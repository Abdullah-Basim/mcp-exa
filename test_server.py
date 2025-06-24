#!/usr/bin/env python3
"""
Test script for Exa MCP Server
"""
import requests
import time

def test_server_health():
    """Test if server is running"""
    try:
        response = requests.get("http://localhost:8000/")
        if response.status_code == 200:
            print("✅ Server is running!")
            print(f"Response: {response.json()}")
            return True
        else:
            print(f"❌ Server returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Is it running?")
        return False

def test_mcp_endpoint():
    """Test the MCP streaming endpoint"""
    try:
        # Test with a simple query
        response = requests.get(
            "http://localhost:8000/mcp",
            params={"query": "What is Python programming"},
            stream=True,
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ MCP endpoint is responding!")
            print("📡 Streaming response:")
            
            # Read first few lines of the stream
            lines_read = 0
            for line in response.iter_lines():
                if line and lines_read < 5:
                    print(f"  {line.decode('utf-8')}")
                    lines_read += 1
                elif lines_read >= 5:
                    break
            
            return True
        else:
            print(f"❌ MCP endpoint returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error testing MCP endpoint: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Exa MCP Server...")
    print("=" * 40)
    
    # Test server health
    if test_server_health():
        time.sleep(1)
        
        # Test MCP endpoint
        test_mcp_endpoint()
    
    print("=" * 40)
    print("�� Test complete!") 