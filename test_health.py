#!/usr/bin/env python3

from app import app
import json

def test_health_endpoint():
    """Test the health endpoint"""
    with app.test_client() as client:
        # Test the health endpoint
        response = client.get('/healthz')
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.get_json()}")
        
        # Verify the response
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert 'timestamp' in data
        
        print("✅ Health endpoint test passed!")

def test_all_endpoints():
    """Test all available endpoints"""
    with app.test_client() as client:
        # Test /oshri endpoint
        response = client.get('/oshri')
        print(f"/oshri Status: {response.status_code}")
        
        # Test /student endpoint
        response = client.get('/student/John')
        print(f"/student/John Status: {response.status_code}")
        
        # Test /healthz endpoint
        response = client.get('/healthz')
        print(f"/healthz Status: {response.status_code}")

def test_health_endpoint_response():
    """Test the health endpoint response format"""
    with app.test_client() as client:
        response = client.get('/healthz')
        data = response.get_json()
        
        print("Health endpoint response format:")
        print(f"  Status: {data.get('status')}")
        print(f"  Message: {data.get('message')}")
        print(f"  Timestamp: {data.get('timestamp')}")
        
        # Verify response format
        required_fields = ['status', 'message', 'timestamp']
        for field in required_fields:
            assert field in data, f"Missing required field: {field}"
        
        print("✅ Health endpoint response format is correct!")

if __name__ == '__main__':
    print("Testing Flask application endpoints...")
    print("=" * 50)
    
    try:
        test_health_endpoint()
        print("\n" + "=" * 50)
        test_all_endpoints()
        print("\n" + "=" * 50)
        test_health_endpoint_response()
        print("\n🎉 All tests passed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        exit(1)
