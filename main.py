import gradio as gr
import ollama

MODEL = "llama2"

system_message = "You are a helpful assistant for that know Science and engineering. "
system_message += "Give short, courteous answers, no more than 1 sentence. "
system_message += "Always be accurate. If you don't know the answer, say so."

def chat(message, history):
    messages = [{"role": "system", "content": system_message}]
    
    for msg in history:
        if isinstance(msg, dict) and 'role' in msg and 'content' in msg:
            content_text = extract_text_from_message(msg['content'])
            messages.append({
                "role": msg['role'], 
                "content": content_text
            })
        elif isinstance(msg, (list, tuple)) and len(msg) == 2:
            user_msg = extract_text_from_message(msg[0])
            assistant_msg = extract_text_from_message(msg[1])
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})
    
    user_content = extract_text_from_message(message)
    messages.append({"role": "user", "content": user_content})

    print("Messages sent to Ollama:", messages) 
    
    response = ollama.chat(model=MODEL, messages=messages)
    return response['message']['content']

def extract_text_from_message(message):
    """Extract text content from Gradio's message format"""
    if isinstance(message, str):
        return message
    elif isinstance(message, list):
        text_parts = []
        for part in message:
            if isinstance(part, dict) and part.get('type') == 'text':
                text_parts.append(part.get('text', ''))
        return ' '.join(text_parts)
    elif isinstance(message, dict):
        if message.get('type') == 'text':
            return message.get('text', '')
    return str(message) 

demo = gr.ChatInterface(fn=chat)
demo.launch()