// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {Test} from "forge-std/Test.sol";
import {TokenVesting} from "../src/TokenVesting.sol";
import {MockToken} from "./MockToken.sol";
import {SafeERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract TokenVestingTest is Test {
    using SafeERC20 for MockToken;

    TokenVesting vesting;
    MockToken token;
    address admin = makeAddr("Admin");
    address beneficiary = makeAddr("Beneficiary");
    address nonBeneficiary = makeAddr("NonBeneficiary");
    uint256 startTime;
    uint256 duration = 30 days;
    uint256 totalAmount = 1000 ether;

    function setUp() public {
        token = new MockToken("Test Token", "TTK");

        // Set start time to 1 day in the future
        startTime = block.timestamp + 1 days;
        vm.startPrank(admin);
        vesting = new TokenVesting(address(token), beneficiary, startTime, duration, totalAmount);

        token.mint(admin, totalAmount);
        token.safeTransfer(address(vesting), totalAmount);
        vm.stopPrank();
    }

    function testClaimBeforeStart() public {
        vm.prank(beneficiary);
        vm.expectRevert(TokenVesting.TokenVesting__vestingNotStarted.selector);
        vesting.claim();
    }

    function testClaimMidVesting() public {
        vm.warp(startTime + 15 days);
        vm.roll(15 days);

        uint256 expectedVested = (totalAmount * 15 days) / duration;
        vm.prank(beneficiary);
        vesting.claim();

        assertEq(vesting.claimedAmount(), expectedVested);
        assertEq(token.balanceOf(beneficiary), expectedVested);
    }

    function testClaimPostVesting() public {
        vm.warp(startTime + duration + 1 days);

        vm.prank(beneficiary);
        vesting.claim();

        assertEq(vesting.claimedAmount(), totalAmount);
        assertEq(token.balanceOf(beneficiary), totalAmount);
    }

    function testMultipleClaims() public {
        // Warp time by 10 days
        vm.warp(startTime + 10 days);
        uint256 firstClaim = (totalAmount * 10 days) / duration;
        vm.prank(beneficiary);
        vesting.claim();
        assertEq(vesting.claimedAmount(), firstClaim);

        vm.warp(startTime + 20 days);
        uint256 secondClaim = (totalAmount * 20 days) / duration - firstClaim;
        vm.prank(beneficiary);
        vesting.claim();
        assertEq(vesting.claimedAmount(), firstClaim + secondClaim);
    }

    function testNonBeneficiaryClaim() public {
        vm.warp(startTime + 15 days);
        vm.prank(nonBeneficiary);
        vm.expectRevert("Only beneficiary can claim");
        vesting.claim();
    }

    function testGetClaimableAmount() public {
        // Before start
        assertEq(vesting.getClaimableAmount(), 0);

        // Mid-vesting
        vm.warp(startTime + 15 days);
        uint256 expectedMid = (totalAmount * 15 days) / duration;
        assertEq(vesting.getClaimableAmount(), expectedMid);

        // Post-vesting
        vm.warp(startTime + duration + 1 days);
        assertEq(vesting.getClaimableAmount(), totalAmount);
    }

    function testTokenTransferFailure() public {
        TokenVesting vestingInsufficient =
            new TokenVesting(address(token), beneficiary, startTime, duration, totalAmount);
        token.safeTransfer(address(vestingInsufficient), totalAmount);

        vm.warp(startTime + 15 days);
        vm.prank(beneficiary);
        vm.expectRevert("Token transfer failed");
        vestingInsufficient.claim();
    }
}
