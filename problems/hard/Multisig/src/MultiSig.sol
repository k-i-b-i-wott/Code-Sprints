// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiSigWallet {
    error Multisig__MustHaveAtleastOneOwner();
    error Multisig__NotAnOwner();
    error Multisig__AlreadyApproved();
    error Multisig__TxAlreadyExecuted();
    error Multisig__NotEnoughApprovals();

    address[] public owners;
    uint256 public requiredApprovals;
    mapping(address => bool) public isOwner;
    mapping(uint256 => mapping(address => bool)) public approvals;

    event TransactionSubmitted(uint256 indexed txId, address indexed to, uint256 value);

    struct Transaction {
        address to;
        uint256 value;
        bool executed;
        uint256 approvalCount;
    }

    Transaction[] public transactions;

    constructor(address[] memory _owners, uint256 _requiredApprovals) {
        if (_owners.length == 0) revert Multisig__MustHaveAtleastOneOwner();
        require(_requiredApprovals > 0 && _requiredApprovals <= _owners.length, "Invalid approvals");

        for (uint i = 0; i < _owners.length; i++) {
            address owner = _owners[i];
            isOwner[owner] = true;
            owners.push(owner);
        }

        requiredApprovals = _requiredApprovals;
    }

    modifier onlyOwners(address _user) {
        if (!isOwner[_user]) revert Multisig__NotAnOwner();
        _;
    }

    function submitWithdrawal(address _to, uint256 _value) external onlyOwners(msg.sender) {
        transactions.push(Transaction({
            to: _to,
            value: _value,
            executed: false,
            approvalCount: 0
        }));
        emit TransactionSubmitted(transactions.length - 1, _to, _value);
    }

    function approveWithdrawal(uint256 _txId) external onlyOwners(msg.sender) {
        Transaction storage txn = transactions[_txId];

        if (txn.executed) revert Multisig__TxAlreadyExecuted();
        if (approvals[_txId][msg.sender]) revert Multisig__AlreadyApproved();

        approvals[_txId][msg.sender] = true;
        txn.approvalCount++;
    }

    function executeWithdrawal(uint256 _txId) external onlyOwners(msg.sender) {
        Transaction storage txn = transactions[_txId];

        if (txn.executed) revert Multisig__TxAlreadyExecuted();
        if (txn.approvalCount < requiredApprovals) revert Multisig__NotEnoughApprovals();

        txn.executed = true;
        (bool success, ) = txn.to.call{value: txn.value}("");
        require(success, "Transfer failed");
    }

    function transactionCount() external view returns (uint256) {
        return transactions.length;
    }

    // Allow contract to receive Ether
    receive() external payable {}
}
