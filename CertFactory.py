

# Server - 20174.1.666.45      Client - 20174.1.666.46

def getPrivateKeyForAddr(addr):
    if addr == "20174.1.666.45":    #Server Key
        with open("/root/Downloads/prashanth.key") as fp:
            private_key_user = fp.read()
        return str.encode(private_key_user)

    if addr == "20174.1.666.46":     #Client Key
        with open("/root/Downloads/prashanth-client.key") as fp:
            private_key_user = fp.read()
        return str.encode(private_key_user)


def getCertsForAddr(address):
    if address == "20174.1.666.45":   #Server ID Certificate
        with open("/root/Downloads/server_cert") as fp:
            id_key_IACA = fp.read()
        return str.encode(id_key_IACA)

    if address == "20174.1.666.46":  #Client ID Certificate
        with open("/root/Downloads/client_cert") as fp:
            id_key_IACA = fp.read()
        return str.encode(id_key_IACA)

    if address == "20174.1.666":   #Intermediate Certificate
        with open("/root/Downloads/paas_signed.cert") as fp:
            pub_key_IACA = fp.read()
        return str.encode(pub_key_IACA)

def getRootCert():
    with open("/root/Downloads/root.crt") as fp:
        root_key_IACA = fp.read()
    return str.encode(root_key_IACA)


#======================================================================================

'''
#Root Certificate
def getRootCertsForAddr():
    with open("/root/Downloads/root.crt") as fp:
        root_key_IACA = fp.read()
    return str.encode(root_key_IACA)

#Intermediate Certificate
def getCertsForAddr():
    with open("/root/Downloads/paas_signed.cert") as fp:
        pub_key_IACA = fp.read()
    return str.encode(pub_key_IACA)

#Client Identity Certificate
def getClientIDCertsForAddr():
    with open("/root/Downloads/client_cert") as fp:
        id_key_IACA = fp.read()
    return str.encode(id_key_IACA)

#Client Private Key
def getClientPrivateKeyForAddr():
    with open("/root/Downloads/prashanth-client.key") as fp:
        private_key_user = fp.read()
    return str.encode(private_key_user)

#Server Identity Certificate
def getServerIDCertsForAddr():
    with open("/root/Downloads/server_cert") as fp:
        id_key_IACA = fp.read()
    return str.encode(id_key_IACA)

#Server Private key
def getServerPrivateKeyForAddr():
    with open("/root/Downloads/prashanth.key") as fp:
        private_key_user = fp.read()
    return str.encode(private_key_user)
'''
