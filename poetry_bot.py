import openai
import os
from typing import Optional

class PoetryChatbot:
    def __init__(self, api_key: str):
        """Initialize the poetry chatbot with OpenAI API key"""
        self.client = openai.OpenAI(api_key=api_key)
    
    def generate_poem(self, prompt: str, style: str = "free verse") -> str:
        """
        Generate a poem based on the given prompt and style
        
        Args:
            prompt (str): The theme or starting word for the poem
            style (str): The style of poem (free verse, haiku, sonnet, etc.)
        
        Returns:
            str: Generated poem
        """
        try:
            # Create a detailed prompt for the AI
            system_prompt = f"""You are a creative poet. Generate a beautiful {style} poem based on the given theme or prompt. 
            Make it creative, emotionally resonant, and well-structured. Keep it between 8-16 lines unless it's a specific form like haiku."""
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Write a poem about: {prompt}"}
                ],
                max_tokens=300,
                temperature=0.8
            )
            
            poem = response.choices[0].message.content.strip()
            return poem
            
        except Exception as e:
            return f"Error generating poem: {str(e)}"

# Example usage and testing
if __name__ == "__main__":
    # Load API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Please set your OPENAI_API_KEY environment variable")
        exit(1)
    
    # Create chatbot instance
    bot = PoetryChatbot(api_key)
    
    # Test the poem generation
    print("Testing Poetry Chatbot...")
    print("-" * 40)
    
    test_prompts = [
        ("sunset", "free verse"),
        ("love", "haiku"),
        ("ocean waves", "free verse")
    ]
    
    for prompt, style in test_prompts:
        print(f"\nPrompt: {prompt} ({style})")
        print("Poem:")
        poem = bot.generate_poem(prompt, style)
        print(poem)
        print("-" * 40)