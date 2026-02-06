"""
Google ADK Agent Demo with Snyk Security Integration

This agent demonstrates a simple customer service assistant with tool capabilities
and AI response validation for safety and quality assurance.
"""

import os
from typing import Any
from google import genai
from google.genai import types
from response_validator import ResponseValidator, ValidationLevel


# Initialize Google Genai client
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Initialize response validator
validator = ResponseValidator(ValidationLevel.STANDARD)

# Model configuration
MODEL_ID = "gemini-2.5-flash-lite"  # Fast, lightweight model with function calling


# Tool Functions
def search_knowledge_base(query: str) -> dict[str, Any]:
    """
    Search the knowledge base for relevant information.
    
    Args:
        query: The search query string
        
    Returns:
        Dictionary containing search results
    """
    # Simulated knowledge base search
    knowledge_base = {
        "shipping": "Standard shipping takes 5-7 business days. Express shipping takes 2-3 business days.",
        "returns": "You can return items within 30 days of purchase for a full refund.",
        "warranty": "All products come with a 1-year manufacturer warranty.",
        "payment": "We accept credit cards, PayPal, and Apple Pay.",
    }
    
    # Simple keyword matching
    query_lower = query.lower()
    results = []
    for topic, info in knowledge_base.items():
        if topic in query_lower or any(word in query_lower for word in topic.split()):
            results.append({"topic": topic, "information": info})
    
    if not results:
        results.append({"topic": "general", "information": "Please contact customer support for more specific information."})
    
    return {"results": results, "query": query}


def check_order_status(order_id: str) -> dict[str, Any]:
    """
    Check the status of a customer order.
    
    Args:
        order_id: The order ID to look up
        
    Returns:
        Dictionary containing order status information
    """
    # Simulated order database
    orders = {
        "ORD-12345": {"status": "shipped", "tracking": "1Z999AA10123456784", "estimated_delivery": "2026-02-05"},
        "ORD-67890": {"status": "processing", "tracking": None, "estimated_delivery": "2026-02-10"},
        "ORD-11111": {"status": "delivered", "tracking": "1Z999AA10123456785", "estimated_delivery": "2026-01-28"},
    }
    
    order_info = orders.get(order_id)
    
    if order_info:
        return {
            "order_id": order_id,
            "status": order_info["status"],
            "tracking_number": order_info["tracking"],
            "estimated_delivery": order_info["estimated_delivery"]
        }
    else:
        return {
            "order_id": order_id,
            "status": "not_found",
            "message": "Order not found. Please verify the order ID."
        }


# Tool declarations for ADK
tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="search_knowledge_base",
                description="Search the knowledge base for information about shipping, returns, warranty, and payment options",
                parameters={
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search query"
                        }
                    },
                    "required": ["query"]
                }
            ),
            types.FunctionDeclaration(
                name="check_order_status",
                description="Check the status of a customer order using the order ID",
                parameters={
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The order ID (format: ORD-XXXXX)"
                        }
                    },
                    "required": ["order_id"]
                }
            )
        ]
    )
]


# Function mapping for tool execution
AVAILABLE_FUNCTIONS = {
    "search_knowledge_base": search_knowledge_base,
    "check_order_status": check_order_status
}


def run_agent(user_message: str) -> str:
    """
    Run the ADK agent with the given user message.
    
    Args:
        user_message: The user's input message
        
    Returns:
        The agent's response as a string
    """
    # System instruction and configuration
    system_instruction = "You are a helpful customer service assistant. Use the available tools to answer customer questions accurately."
    
    # Create chat with tools
    chat = client.chats.create(
        model=MODEL_ID,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            tools=tools,
            temperature=0.7
        )
    )
    
    # Send user message
    response = chat.send_message(user_message)
    
    # Handle function calls in a loop
    max_iterations = 5  # Prevent infinite loops
    iteration = 0
    
    while iteration < max_iterations:
        # Check if there's a function call in the response
        if not response.candidates:
            break
            
        parts = response.candidates[0].content.parts
        if not parts:
            break
            
        # Look for function calls
        function_calls = [part for part in parts if hasattr(part, 'function_call') and part.function_call]
        
        if not function_calls:
            # No more function calls, we have the final response
            break
        
        # Process function calls
        function_responses = []
        for part in function_calls:
            function_call = part.function_call
            function_name = function_call.name
            function_args = dict(function_call.args) if function_call.args else {}
            
            # Execute the function
            if function_name in AVAILABLE_FUNCTIONS:
                function_result = AVAILABLE_FUNCTIONS[function_name](**function_args)
                function_responses.append(
                    types.Part(
                        function_response=types.FunctionResponse(
                            name=function_name,
                            response=function_result
                        )
                    )
                )
        
        # Send function results back
        if function_responses:
            response = chat.send_message(
                types.Content(parts=function_responses)
            )
        else:
            break
            
        iteration += 1
    
    # Extract text from final response
    if response.candidates and response.candidates[0].content.parts:
        text_parts = [part.text for part in response.candidates[0].content.parts if hasattr(part, 'text')]
        final_response = ' '.join(text_parts) if text_parts else "I apologize, but I couldn't generate a response."
    else:
        final_response = "I apologize, but I couldn't generate a response."
    
    # Validate the response before returning
    validation_result = validator.validate_response(
        response=final_response,
        query=user_message,
        context={'tools_used': iteration > 0}
    )
    
    # Log validation results (in production, send to monitoring)
    if not validation_result.is_safe or validation_result.confidence_score < 0.7:
        print(f"\n⚠️  Response Validation Warning:")
        print(f"   Safe: {validation_result.is_safe}")
        print(f"   Accurate: {validation_result.is_accurate}")
        print(f"   Relevant: {validation_result.is_relevant}")
        print(f"   Confidence: {validation_result.confidence_score:.2f}")
        if validation_result.issues:
            print(f"   Issues: {', '.join(validation_result.issues)}")
    
    return final_response


def main():
    """Main function to run the agent."""
    print("🤖 Google ADK Customer Service Agent")
    print("=" * 50)
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            response = run_agent(user_input)
            print(f"\n🤖 Agent: {response}\n")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()
