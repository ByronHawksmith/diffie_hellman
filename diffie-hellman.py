def client_step_one(P, a, G):
    # client computes public value of x
    x = pow(G, a) % P

    # client notifies client of public value of x
    return x


def server_step_one(G, b, P):
    # server computes public value of y
    y = pow(G, b) % P

    # server notifies client of public value of y
    return y


def client_step_two(y, a, P):
    # client computes symmetric key (KeyA)
    key_a = pow(y, a) % P

    # compare keys
    return key_a


def server_step_two(x, b, P):
    # server computes symmetric key (KeyB)
    key_b = pow(x, b) % P

    # compare keys
    return key_b


G = 69  # server pub key
b = 958  # server priv key
P = 3213  # client pub key
a = 5  # client priv key

x = client_step_one(P, a, G)
y = server_step_one(G, b, P)

key_a = client_step_two(y, a, P)
key_b = server_step_two(x, b, P)

print(key_a)
print(key_b)
