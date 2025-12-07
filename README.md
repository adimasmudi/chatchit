# ChatChit - Science & Engineering Assistant

A web-based chatbot application that uses the Llama2 model through Ollama to answer questions related to science and engineering.

## Prerequisites

Make sure you have installed:

- Python 3.8+
- [Ollama](https://ollama.ai/)

## Project Setup

### 1. Clone or Download Project

```bash
git clone https://github.com/adimasmudi/chatchit.git
cd chatchit
```

### 2. Setup Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# For Linux/Mac:
source .venv/bin/activate

# For Windows:
# .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Ollama & Llama2

```bash
# Install Llama2 model (if not already available)
ollama pull llama2

# Verify model is available
ollama list
```

## Running the Project

### 1. Ensure Virtual Environment is Active

```bash
source .venv/bin/activate
```

### 2. Run the Application

```bash
python main.py
```

### 3. Access the Application

Open your browser and visit: `http://127.0.0.1:7860`

## Project Structure

```
chatchit/
├── main.py              # Main application file
├── test_ollama.py       # Ollama connection test script
├── requirements.txt     # Dependencies list
├── README.md           # This documentation
└── .venv/              # Virtual environment
```

## Dependencies

- `gradio` - Framework for creating web interfaces
- `ollama` - Python client for Ollama

## Troubleshooting

### Error: Model not found

```bash
ollama pull llama2
```

### Error: Ollama not running

Make sure Ollama service is running:

```bash
ollama serve
```

### Error: Port already in use

Edit `main.py` and change the port in `demo.launch()`:

```python
demo.launch(server_port=7861)
```

## Customization

### Changing Model

Edit the `MODEL` variable in `main.py`:

```python
MODEL = "llama3.2"  # or any other available model
```

### Changing System Message

Edit the `system_message` variable in `main.py` to change the assistant's personality.

## Testing

Test Ollama connection:

```bash
python test_ollama.py
```

## License

MIT License
