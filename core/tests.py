from django.test import TestCase

# Create your tests here.
from intasend import APIService

# Replace these with your actual token and publishable key
token = "ISSecretKey_test_493e0ea5-c804-461f-ad31-f905b918ec64"
publishable_key = "ISPubKey_test_59994385-e1ca-401c-a249-08cbfe184e40"

# Initialize the API service (set test=True for sandbox environment)
service = APIService(token=token, publishable_key=publishable_key, test=True)

# Payment payload details
checkout_data = {
    "amount": 10,
    "currency": "KES",
    "email": "customer@example.com",
    "phone_number": "254722424220",
    "first_name": "Ian",
    "last_name": "Koech",
    "api_ref": "ORDER-12345",  # Unique reference for your system
    "redirect_url": "http://evalastmotorcycles.com/success",  # URL to redirect after payment
}

# Generate the checkout link
checkout_response = service.checkout.create(data=checkout_data)

# Check response
if checkout_response['status'] == 'success':
    # Get the checkout link
    checkout_url = checkout_response['data']['url']
    print(f"Send this checkout link to the customer: {checkout_url}")
else:
    print("Failed to generate checkout link:", checkout_response)
