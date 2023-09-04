import hashlib


# function which hashes the URL entered by the user
def hash_url(long_url):
    m = hashlib.md5(long_url.encode('utf-8'))
    hashed = m.hexdigest()
    return hashed[:7]
