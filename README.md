# Python Playground

A small sandbox for experimenting with Python snippets, testing ideas, and exploring libraries without the overhead of a full project setup. Nothing here is meant to be polished—just a place to try things out.

## Features

- Minimal structure
- Quick experiments without boilerplate
- Optional virtual environment support
- Space for notebooks, scratch scripts, and prototypes

## Getting Started
1. Clone the repo
``` bash
git clone https://github.com/QuantumJunction/PythonPlayground.git
cd PythonPlayground
```

2. Set up a virtual environment (recommended)
``` bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

3. Install dependencies (if any)
``` bash
pip install -r requirements.txt
``` 

If no requirements file exists yet, create one when needed:
``` bash
pip freeze > requirements.txt
``` 

## Structure
``` bash
/
├── experiments/     # Scratch scripts, prototypes
├── notebooks/       # Jupyter notebooks for exploration
├── utils/           # Helper modules
├── requirements.txt # dependencies
├── LICENSE
└── README.md
``` 

## Usage

Run any script:
``` bash
python experiments/<script>.py
``` 

Start Jupyter:
``` bash
jupyter notebook
``` 

## Guidelines

- Commit only what might be useful later.
- Remove clutter when it stops being useful.
- Keep experiments isolated so they don’t interfere with each other.


