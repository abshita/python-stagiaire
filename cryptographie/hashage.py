# Hashage simple avec sha256
import hashlib

message = "bonjour"
resultat = hashlib.sha256(message.encode()).hexdigest()
print("Message:", message)
print("SHA256:", resultat)
