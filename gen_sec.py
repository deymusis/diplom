import random
import string

def generate_secret_key(length=50):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

new_secret_key = generate_secret_key()
print(new_secret_key)
