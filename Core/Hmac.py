import hashlib
import hmac
import base64

# message = bytes('Message', 'utf-8')
# secret = bytes('secret', 'utf-8')

merchant_sharekey = "79a9afb0d786c3c4aba02d455d20a7ac"
message = "{\"TransactionType\": 0, \"BankCode\":\"STB\",\"CashAmount\": 100000.0, \"PaymentMethod\": 0, \"Os\":0, \"RequestTimestamp\": 1581384548, \"Version\" : \"2.2.5\", \"Language\": 1}"
secret = merchant_sharekey + ":P@y00:" + "609"
secret = bytes(secret,'utf-8')
message = bytes(message, 'utf-8')
print(secret)
print(message)

signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
print(signature)