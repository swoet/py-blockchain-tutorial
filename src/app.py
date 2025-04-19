from flask import Flask, jsonify, request
from uuid import uuid4
from src.blockchain import Blockchain

# Instantiate the node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # Run PoW algorithm to get next proof
    last_proof = blockchain.last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Reward for finding the proof
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new Block
    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.new_block(proof, previous_hash)

    return jsonify({
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(
        values['sender'], values['recipient'], values['amount']
    )
    return jsonify({'message': f'Transaction will be added to Block {index}'}), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    return jsonify({
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()
    nodes = values.get('nodes')
    if nodes is None:
        return "Error: supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)
    return jsonify({
        'message': 'New nodes added',
        'total_nodes': list(blockchain.nodes)
    }), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()
    if replaced:
        msg = 'Chain was replaced'
    else:
        msg = 'Our chain is authoritative'
    return jsonify({
        'message': msg,
        'chain': blockchain.chain
    }), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to your Python Blockchain API!",
        "endpoints": [
            "/mine", "/transactions/new", "/chain",
            "/nodes/register", "/nodes/resolve"
        ]
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
