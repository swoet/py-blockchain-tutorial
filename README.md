# 🔗 Python Blockchain Tutorial

A lightweight Python-based blockchain framework with Proof of Work, a RESTful API using Flask, and basic peer-to-peer consensus capabilities.

This project is great for learning how blockchains work under the hood.

---

## 🚀 Features

- Block creation and SHA-256 hashing
- Proof of Work mining algorithm
- Transaction queue and validation
- Flask-powered API to interact with the chain
- Register and sync multiple nodes (consensus)
- Clean modular structure and testable components

---

## 📦 Project Structure

```
py-blockchain-tutorial/
│
├── src/                        # Source files
│   ├── app.py                  # Flask API
│   └── blockchain.py      # Core blockchain logic
│
├── tests/                      # Unit tests
│   └── test_blockchain.py      # Blockchain unit tests
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 📑 Installation

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/py-blockchain-tutorial.git
cd py-blockchain-tutorial
```

### Install dependencies

Create a virtual environment and install the required Python dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

---

## 🛠️ Usage

### Running the Flask API

To start the Flask API, run the following command:

```bash
python src/app.py
```

This will start the server on `http://localhost:5000` by default. You can interact with the blockchain using the RESTful API provided by the application.

### Available API Endpoints

- `GET /chain`: Get the current blockchain.
- `POST /transactions/new`: Add a new transaction to the queue.
- `GET /mine`: Mine a new block.
- `GET /nodes/register`: Register a new node with the network.
- `GET /nodes/resolve`: Resolve conflicts between nodes (consensus).

---

## 🧪 Running Tests

To run the tests, use the following command:

```bash
pytest tests/test_blockchain.py
```

---

## 📚 Dependencies

This project requires the following Python libraries:

- `Flask`
- `requests`
- `hashlib`
- `json`
- `pytest`

You can install them with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

