# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
verify_sid = os.getenv("verify_sid")
verified_number = os.getenv("verified_number")

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)