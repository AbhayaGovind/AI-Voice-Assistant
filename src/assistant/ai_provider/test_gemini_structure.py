"""
Test file to verify Gemini provider structure without requiring google-generativeai
"""


# Mock the google.generativeai import for testing
class MockGenAI:
    def configure(self, api_key):
        pass

    class GenerativeModel:
        def __init__(self, model_name):
            self.model_name = model_name

        def generate_content(self, content):
            class MockResponse:
                text = f"Mock response for: {content if isinstance(content, str) else 'conversation'}"

            return MockResponse()


import sys

sys.modules["google.generativeai"] = MockGenAI()

# Now import our Gemini class
from gemini import Gemini


def test_gemini_structure():
    print("🧪 Testing Gemini provider structure...")

    # Test with mock API key
    gemini = Gemini("mock-api-key")

    print(f"✅ Name: {gemini.name}")
    print(f"✅ Temperature: {gemini.temperature}")
    print(f"✅ Max tokens: {gemini.max_tokens}")
    print(f"✅ Model: {gemini.model.model_name}")

    # Test the ask method
    response = gemini.ask("Hello, test message")
    print(f"✅ Response received: {response[:50]}...")

    print("\n🎉 Gemini provider structure test successful!")


if __name__ == "__main__":
    test_gemini_structure()
