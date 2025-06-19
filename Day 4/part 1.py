import hashlib

key = open('input', 'r').read()
count = 0

hash = hashlib.md5(key.encode('UTF-8')).hexdigest()

while hash[:5] != '00000':
    count += 1
    keyAndCount = key + str(count)
    hash = hashlib.md5(keyAndCount.encode('UTF-8')).hexdigest()

print(count)
