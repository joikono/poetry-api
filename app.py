from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from poetry_bot import PoetryChatbot

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Initialize the poetry chatbot
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required")

poetry_bot = PoetryChatbot(api_key)

@app.route('/')
def home():
    """Basic home endpoint"""
    return jsonify({
        "message": "Poetry API is running!",
        "endpoints": {
            "generate_poem": "/api/poem?prompt=your_theme&style=free_verse"
        }
    })

@app.route('/api/poem', methods=['GET'])
def generate_poem():
    """
    Generate a poem based on query parameters
    
    Query Parameters:
        prompt (str): The theme or topic for the poem
        style (str, optional): The style of poem (default: "free verse")
    
    Returns:
        JSON response with the generated poem
    """
    try:
        # Get parameters from query string
        prompt = request.args.get('prompt')
        style = request.args.get('style', 'free verse')
        
        # Validate prompt
        if not prompt:
            return jsonify({
                "error": "Missing required parameter 'prompt'",
                "example": "/api/poem?prompt=sunset&style=haiku"
            }), 400
        
        # Generate the poem
        poem = poetry_bot.generate_poem(prompt, style)
        
        # Return successful response
        return jsonify({
            "success": True,
            "prompt": prompt,
            "style": style,
            "poem": poem,
            "timestamp": "2025-05-25"  # You could use datetime.now() for real timestamp
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Internal server error: {str(e)}"
        }), 500

@app.route('/api/poem', methods=['POST'])
def generate_poem_post():
    """
    Generate a poem using POST request with JSON data
    
    Request Body:
        {
            "prompt": "theme or topic",
            "style": "poem style (optional)"
        }
    
    Returns:
        JSON response with the generated poem
    """
    try:
        # Get JSON data from request body
        data = request.get_json()
        
        if not data:
            return jsonify({
                "error": "Request must contain JSON data"
            }), 400
        
        prompt = data.get('prompt')
        style = data.get('style', 'free verse')
        
        # Validate prompt
        if not prompt:
            return jsonify({
                "error": "Missing required field 'prompt'"
            }), 400
        
        # Generate the poem
        poem = poetry_bot.generate_poem(prompt, style)
        
        # Return successful response
        return jsonify({
            "success": True,
            "prompt": prompt,
            "style": style,
            "poem": poem,
            "timestamp": "2025-05-25"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Internal server error: {str(e)}"
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "error": "Endpoint not found",
        "available_endpoints": ["/", "/api/poem"]
    }), 404

if __name__ == '__main__':
    print("Starting Poetry API server...")
    print("Available endpoints:")
    print("  GET  /              - API info")
    print("  GET  /api/poem      - Generate poem with query params")
    print("  POST /api/poem      - Generate poem with JSON body")
    print("\nExample usage:")
    print("  curl 'http://localhost:5000/api/poem?prompt=ocean&style=haiku'")
    
    app.run(debug=True, host='0.0.0.0', port=5000)