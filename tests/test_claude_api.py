#!/usr/bin/env python3
"""
🧪 Claude API Key Test Script
Simple test to verify your Anthropic Claude API key is working correctly.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_claude_api():
    """Test Claude API key with a simple request"""
    
    # Check if API key is set
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not found in environment variables")
        print("💡 Please set your API key:")
        print("   export ANTHROPIC_API_KEY='your-api-key-here'")
        print("   Or add it to your .env file")
        return False
    
    print(f"✅ API key found: {api_key[:10]}...{api_key[-4:]}")
    
    # Test the API
    try:
        import anthropic
        
        # Initialize client
        client = anthropic.Anthropic(api_key=api_key)
        
        print("🔄 Testing Claude API connection...")
        
        # Simple test message
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=50,
            messages=[
                {"role": "user", "content": "Hello! Please respond with just 'API test successful' if you can read this."}
            ]
        )
        
        response_text = message.content[0].text.strip()
        print(f"🤖 Claude Response: {response_text}")
        
        if "API test successful" in response_text.lower() or "successful" in response_text.lower():
            print("🎉 SUCCESS: Claude API is working perfectly!")
            return True
        else:
            print("⚠️  API connected but unexpected response")
            return True
            
    except ImportError:
        print("❌ ERROR: 'anthropic' library not installed")
        print("💡 Install it with: pip install anthropic")
        return False
        
    except anthropic.AuthenticationError:
        print("❌ ERROR: Invalid API key")
        print("💡 Please check your ANTHROPIC_API_KEY")
        return False
        
    except anthropic.RateLimitError:
        print("❌ ERROR: Rate limit exceeded")
        print("💡 Please wait a moment and try again")
        return False
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

def main():
    """Main test function"""
    print("🧪 Claude API Key Test")
    print("=" * 40)
    
    success = test_claude_api()
    
    print("\n" + "=" * 40)
    if success:
        print("✅ Test completed successfully!")
        print("🚀 Your Claude API key is ready to use!")
    else:
        print("❌ Test failed - please check your API key setup")
        sys.exit(1)

if __name__ == "__main__":
    main() 