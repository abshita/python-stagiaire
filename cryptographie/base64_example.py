# Encodage Base64
import base64

message = "secret"
code = base64.b64encode(message.encode())
print("Message:", message)
print("Base64:", code.decode())

original = base64.b64decode(code)
print("Décodé:", original.decode())
