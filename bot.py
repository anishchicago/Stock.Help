from factom_api import create_chain, chain_search
from sign_verify import generate_key, sign, verify

def create_bot():
    public_key = generate_key('bot').decode()
    data = sign(username='bot',public_key=public_key)
    return(create_chain(external_ids=['bot'], content=str(data))['chain_id'])

print(create_bot())