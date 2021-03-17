P = 23  # client pub key
a = 4  # client priv key
G = 9  # server pub key
b = 3  # server priv key

# client knows servers public num
# server knows client public num

# client computes public value of x
x = pow(G, a) % P

# server computed public value of y
y = pow(G, b) % P

# client computes symmetric key (KeyA)
key_a = pow(y, a) % P

# server computes symmetric key (KeyB)
key_b = pow(x, b) % P

print(key_a)
print(key_b)
