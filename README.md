Poetry API 
A creative poetry generation API powered by OpenAI's GPT model, built with Flask and featuring a beautiful web interface.
Features 

AI-Powered Poetry Generation: Create beautiful poems using OpenAI's GPT model
Multiple Poetry Styles: Support for various poetry forms (free verse, haiku, sonnet, limerick, ballad, acrostic)
RESTful API: Clean API endpoints with both GET and POST support
Web Interface: Beautiful, responsive frontend for easy interaction
CORS Enabled: Ready for frontend integration
Error Handling: Comprehensive error handling and validation
Flexible Input: Accept themes and topics as prompts

Prerequisites 

Python 3.7+
OpenAI API key
Modern web browser (for frontend interface)

Installation 

Clone or download the project files
bash# If using git
git clone <your-repo-url>
cd poetry-api

Create a virtual environment (recommended)
bashpython -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

Install required packages
bashpip install flask flask-cors openai

Set up environment variables
Create a .env file in the project root:
bashOPENAI_API_KEY=your_openai_api_key_here
Or set it directly in your environment:
bash# Windows Command Prompt
set OPENAI_API_KEY=your_openai_api_key_here

# Windows PowerShell
$env:OPENAI_API_KEY="your_openai_api_key_here"

# macOS/Linux
export OPENAI_API_KEY=your_openai_api_key_here


Getting Your OpenAI API Key 

Visit OpenAI's website
Sign up or log in to your account
Navigate to the API section
Generate a new API key
Copy and use it in your environment variables

Usage
Starting the Server
bashpython app.py
The server will start on http://localhost:5000
You should see output like:
Starting Poetry API server...
Available endpoints:
  GET  /              - API info
  GET  /api/poem      - Generate poem with query params
  POST /api/poem      - Generate poem with JSON body

Example usage:
  curl 'http://localhost:5000/api/poem?prompt=ocean&style=haiku'
Using the Web Interface

Open your web browser
Navigate to the project directory
Open index.html in your browser
Start generating poems!

The web interface provides:

Input field for poem topics/themes
Dropdown for poetry styles
Real-time poem generation
API status checking
Responsive design for mobile devices

API Endpoints 📡
GET /
Returns basic API information and available endpoints.
Response:
json{
  "message": "Poetry API is running!",
  "endpoints": {
    "generate_poem": "/api/poem?prompt=your_theme&style=free_verse"
  }
}
GET /api/poem
Generate a poem using query parameters.
Parameters:

prompt (required): The theme or topic for the poem
style (optional): Poetry style (default: "free verse")

Example:
bashcurl "http://localhost:5000/api/poem?prompt=sunset&style=haiku"
Response:
json{
  "success": true,
  "prompt": "sunset",
  "style": "haiku",
  "poem": "Golden rays descend\nPainting clouds in crimson hues\nDay surrenders night",
  "timestamp": "2025-05-25"
}
POST /api/poem
Generate a poem using JSON request body.
Request Body:
json{
  "prompt": "ocean waves",
  "style": "free verse"
}
Response:
json{
  "success": true,
  "prompt": "ocean waves",
  "style": "free verse",
  "poem": "Endless blue expanse\nWaves dancing with the wind...",
  "timestamp": "2025-05-25"
}
Supported Poetry Styles

Free Verse: Flexible, modern poetry without strict rules
Haiku: Traditional Japanese 3-line, 5-7-5 syllable structure
Sonnet: 14-line poem with specific rhyme scheme
Limerick: Humorous 5-line poem with AABBA rhyme scheme
Ballad: Narrative poem, often telling a story
Acrostic: Poem where first letters spell out a word

Example Usage with curl 
bash# Simple haiku about nature
curl "http://localhost:5000/api/poem?prompt=mountain&style=haiku"

# Free verse about love
curl "http://localhost:5000/api/poem?prompt=love&style=free%20verse"

# POST request with JSON
curl -X POST http://localhost:5000/api/poem \
  -H "Content-Type: application/json" \
  -d '{"prompt": "stars", "style": "sonnet"}'
Project Structure
poetry-api/
├── app.py              # Flask API server
├── poetry_bot.py       # Poetry generation logic
├── index.html          # Web frontend interface
├── .gitignore         # Git ignore rules
├── .env               # Environment variables (create this)
└── README.md          # This file
Error Handling 
The API includes comprehensive error handling:

400 Bad Request: Missing or invalid parameters
500 Internal Server Error: OpenAI API errors or server issues
404 Not Found: Invalid endpoints

Example error response:
json{
  "success": false,
  "error": "Missing required parameter 'prompt'",
  "example": "/api/poem?prompt=sunset&style=haiku"
}
Development Tips 

Testing the Poetry Bot: Run python poetry_bot.py to test poem generation directly
CORS Issues: The API includes CORS headers for frontend development
API Key Security: Never commit your .env file or expose your API key
Rate Limits: Be aware of OpenAI's API rate limits and usage costs

Customization Options 
Modify Poetry Styles
Edit the generate_poem method in poetry_bot.py to add custom poetry styles or modify existing ones.
Update Frontend
The index.html file can be customized with:

Different styling and themes
Additional input fields
Custom poetry style options
Enhanced error handling

Extend API Endpoints
Add new endpoints in app.py for features like:

Poem history storage
User accounts
Poem rating/feedback
Batch poem generation

Troubleshooting 🔧
Common Issues

"OPENAI_API_KEY environment variable is required"

Make sure you've set your OpenAI API key in the environment


"Connection refused" errors

Ensure the Flask server is running on port 5000
Check if another application is using port 5000


CORS errors in browser

Make sure CORS is enabled in app.py (it should be by default)
Check that you're accessing the correct URL


OpenAI API errors

Verify your API key is valid and has sufficient credits
Check OpenAI's service status



Contributing 

Fork the repository
Create a feature branch
Make your changes
Test thoroughly
Submit a pull request

License 📄
This project is open source. Feel free to use, modify, and distribute as needed.
Support 💬
If you encounter any issues or have questions:

Check the troubleshooting section above
Verify your OpenAI API key and setup
Ensure all dependencies are properly installed


Happy Poetry Generation! 
