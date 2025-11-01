# AI Chatbot Widget

Simple AI chatbot widget built with Flask and OpenAI API.

## Features

- OpenAI GPT integration
- Responsive chat interface
- Customizable design
- Standalone web application

## Prerequisites

- Python 3.8+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/ai-chatbot-widget.git
cd ai-chatbot-widget
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key_here
ASSISTANT_NAME=Ava
ASSISTANT_STYLE=Be concise, practical, friendly and respond in preferred language.
```

5. (Optional) Customize prompts:
Edit `prompt-sample.txt` to modify the assistant's behavior.

## Usage

Run the application:
```bash
python app.py
```

Open your browser at `http://localhost:8000`

## Project Structure
```
ai-chatbot-widget/
├── app.py                  # Flask server
├── chat-widget.html        # Chat widget interface
├── prompt-sample.txt       # AI assistant instructions
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `ASSISTANT_NAME` | Assistant name | `Ava` |
| `ASSISTANT_STYLE` | Communication style | See `.env` |

### Customizing Appearance

Edit `chat-widget.html`:
- Colors: Search for `#faae77`, `#ffe7d6`, `#dcead2`
- Font: Change `Roboto Mono` to another Google Font
- Dimensions: Adjust `max-width`, `height` in CSS

## API Endpoints

- `GET /` - Redirects to chat widget
- `GET /chat-widget.html` - Chat widget interface
- `POST /chat` - Send message to AI
  - Request body: `{"message": "your message"}`
  - Response: `{"response": "AI response", "status": "success"}`

## Tech Stack

- Backend: Flask, OpenAI Python SDK
- Frontend: HTML, Vanilla JavaScript, CSS
- Font: Roboto Mono

## Security Notes

- Never commit `.env` file with API keys
- Use environment variables in production
- Consider adding rate limiting for production use
- Implement authentication if exposing publicly

## Troubleshooting

**Issue: "Missing OPENAI_API_KEY in .env file"**
- Make sure `.env` file exists in root directory
- Check that `OPENAI_API_KEY` is set correctly

**Issue: "chat-widget.html not found"**
- Verify `chat-widget.html` is in the same directory as `app.py`

**Issue: CORS errors**
- Flask-CORS is already configured, but check browser console for details

## License

MIT License - feel free to use, modify, and distribute.

## Contributing

Pull requests welcome. For major changes, open an issue first.

## Support

For issues or questions, open an issue on GitHub.