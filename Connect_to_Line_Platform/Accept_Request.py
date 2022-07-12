import base64
import hashlib
import hmac

channel_secret = 'd79a825ec7d0940a59ac9507ad75cac7' # Channel secret string
body = '...' # Request body string
hash = hmac.new(channel_secret.encode('utf-8'),
    body.encode('utf-8'), hashlib.sha256).digest()
signature = base64.b64encode(hash)
# Compare x-line-signature request header and the signature