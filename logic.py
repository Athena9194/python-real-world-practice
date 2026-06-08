import random
import string

url_storage = {}


def generate_short_code(length=5):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def save_url(long_url, expiration="30d"):
    short_code = generate_short_code()
    url_storage[short_code] = {
        "url" : long_url,
        "expiration" : expiration
    }
    return short_code

