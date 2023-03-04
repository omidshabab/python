# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC41678a548e89c03acda1f41db2487cfe"
auth_token = "ff9dfc5e52ee89c49ad2fcbc8d93c509"
verify_sid = "VAe25e5180c263fef55fa40561d0f5d833"
verified_number = "+989934901913"

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