import pytest
from src.blockchain import Blockchain

def test_new_block_and_transaction():
    bc = Blockchain()
    # initial chain length is 1 (genesis)
    assert len(bc.chain) == 1

    # add a transaction
    idx = bc.new_transaction('a', 'b', 5)
    assert idx == 2  # will be added to block index 2

    # mine a new block
    proof = bc.proof_of_work(bc.last_block['proof'])
    block = bc.new_block(proof)
    assert block['index'] == 2
    assert len(bc.chain) == 2
