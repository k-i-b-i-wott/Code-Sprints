// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {SafeERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract TokenVesting {
    using SafeERC20 for IERC20;

    error TokenVesting__vestingNotStarted();

    IERC20 public token;
    address public admin;
    address public beneficiary;
    uint256 public startTime;
    uint256 public duration;
    uint256 public totalAmount;
    uint256 public claimedAmount;

    event TokensClaimed(address indexed beneficiary, uint256 amount);

    constructor(
        address _token,
        address _beneficiary,
        uint256 _startTime,
        uint256 _duration,
        uint256 _totalAmount
    ) {
        require(_token != address(0), "Invalid token address");
        require(_beneficiary != address(0), "Invalid beneficiary");
        require(_duration > 0, "Duration must be greater than 0");
        require(_totalAmount > 0, "Amount must be greater than 0");

        token = IERC20(_token);
        beneficiary = _beneficiary;
        startTime = _startTime;
        duration = _duration;
        totalAmount = _totalAmount;
        admin = msg.sender;

        // // Transfer tokens from admin to vesting contract
        // token.approve(address(this), _totalAmount);
        // token.safeTransferFrom(msg.sender, address(this), _totalAmount);
    }

    function claim() public {
        if (block.timestamp < startTime) revert TokenVesting__vestingNotStarted();
        require(msg.sender == beneficiary, "Only beneficiary can claim");

        uint256 claimable = getClaimableAmount();
        require(claimable > 0, "No tokens to claim");

        claimedAmount += claimable;
        token.safeTransfer(beneficiary, claimable);

        emit TokensClaimed(beneficiary, claimable);
    }

    function _calculateVestedAmount() private view returns (uint256) {
        if (block.timestamp < startTime) {
            return 0;
        } else if (block.timestamp >= startTime + duration) {
            return totalAmount;
        } else {
            uint256 elapsedTime = block.timestamp - startTime;
            return (totalAmount * elapsedTime) / duration;
        }
    }

    function getClaimableAmount() public view returns (uint256) {
        uint256 vested = _calculateVestedAmount();
        return vested - claimedAmount;
    }
}
