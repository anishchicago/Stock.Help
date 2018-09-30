
import ed25519
import json

# REFERENCED https://github.com/stackdump/factom-smartcontract-demo/blob/master/src/game.py

def generate_key(prefix):
    """ generate a private key """
    signing_key, verifying_key = ed25519.create_keypair()
    filename = prefix + "-secret-key.txt"
    open(filename, "wb").write(signing_key.to_bytes())
    print('wrote ' + filename)
    vkey_hex = verifying_key.to_ascii(encoding="hex")
    print(prefix + " public key is", vkey_hex)
    return vkey_hex

def _signing_key(name, prefix=None):
    """
    helper to load signing keys from filesystem
    NOTE: keys must already be present  see: ./src/gen_keys.py
    """
    keydata = open(prefix + name + "-secret-key.txt","rb").read()
    return ed25519.SigningKey(keydata)


def sign(**event):
    SIGNING_KEYS = {event['username']: _signing_key(event['username'], '')}
    """ sign event data """
    key = SIGNING_KEYS[event['username']]
    data = json.dumps(event)
    return  {
        'event': data,
        'sig': key.sign(bytes(data, 'utf-8')).hex()
    }

def verify(**payload):
    """ raises ed25519.BadSignatureError an exception on invalid signature """
    event = json.loads(payload['event'])
    try:
        verify_key = event['verify_key'].to_bytes()
    except:
        SIGNING_KEYS = {event['username']: _signing_key(event['username'], '')}
        verify_key = SIGNING_KEYS[event['username']].get_verifying_key()
    verify_key.verify(bytes.fromhex(payload['sig']), bytes(payload['event'], 'utf-8'))
    return True