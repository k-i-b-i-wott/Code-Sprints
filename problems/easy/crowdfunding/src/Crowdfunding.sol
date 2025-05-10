// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Crowdfunding {
    uint256 public goal;
    uint256 public deadline;
    uint256 public totalRaised;
    address public creator;
    mapping(address => uint256) public contributions;

    constructor(uint256 _goal, uint256 _deadline) {
        require(_goal > 0, "Goal must be greater than zero");
        require(_deadline > block.timestamp, "Deadline must be in the future");

        goal = _goal;
        deadline = _deadline;
        creator = msg.sender;
    }

    function donate() public payable {
        require(block.timestamp < deadline, "Campaign has ended");
        require(msg.value > 0, "Donation must be greater than zero");

        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;
    }

    function withdraw() public {
        if (msg.sender == creator) {
            // Creator withdraws funds if the goal is met
            require(totalRaised >= goal, "Goal not reached");
            require(block.timestamp >= deadline, "Campaign is still active");

            uint256 amount = totalRaised;
            totalRaised = 0;
            (bool success, ) = creator.call{value: amount}("");
            require(success, "Transfer to creator failed");
        } else {
            // Donors withdraw their contributions if the goal is not met
            require(block.timestamp >= deadline, "Campaign is still active");
            require(totalRaised < goal, "Goal was reached"); // Ensure goal was not reached

            uint256 amount = contributions[msg.sender];
            require(amount > 0, "No contributions to withdraw");

            contributions[msg.sender] = 0;
            totalRaised -= amount; // Decrement totalRaised when a donor withdraws
            (bool success, ) = msg.sender.call{value: amount}("");
            require(success, "Refund failed");
        }
    }
}
