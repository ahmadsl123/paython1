from hashlib import sha256
from tronpy import Tron
from tronpy.keys import PrivateKey
import numpy as np

class Mining:
    def __init__(self, address,key):
        self.address = address
        self.key=key
        self.current_transactions = []
        self.chain = []
        self.new_block(previous_hash='1')

    def new_block(self, previous_hash):

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []

        self.chain.append(block)
        return block
    def validation(self,number, transactions, previous_hash):
       str = '0'*5
       for nonce1 in range(nonce):
          text = str(number) + transactions + previous_hash + str(nonce1)
          hash = sha256(text.encode("ascii")).hexdigest()
          if hash.startswith(str):
              print(f"Bitcoin with nonce value:{nonce1}")
              return hash

       raise BaseException("Error")
    def connection(self,amount, account):
        try:
            priv = PrivateKey(bytes.fromhex(key))

            # create transaction
            trn = (
                client.trx.transfer(address, str(account), int(amount))
                    .memo("Transaction")
                    .build()
                    .inspect()
                    .sign(priv)
                    .broadcast()
            )
            return trn.wait()

        # return the exception
        except Exception as ex:
            return ex

class Check_valid:

    # init method
    def __init__(self, nonce):
        self.nonce = nonce
    def encode(self,text):
        return sha256(text.encode("ascii")).hexdigest()

    def transaction(self,number, transactions, previous_hash, prefix_zeros):
       prefix_str = '0'*prefix_zeros
       for nonce1 in range(nonce):
          text = str(number) + transactions + previous_hash + str(nonce1)
          new = self.encode(text)
          if new.startswith(prefix_str):
              print(f"Bitcoin with nonce value:{nonce1}")
              return new

       raise BaseException(f"Error:  Couldn't find correct has after trying {nonce} times")

if __name__=='__main__':
    transactions='''
    Johnny->depp->30,
    Amber->Heard->40
    '''
    level=4 # try changing this to higher number and you will see it will take more time for mining
    import time
    nonce = 1000000000000
    halftron = 200000
    onetron = 5000000

    # your account information
    account_ADDRESS = "29568d0cff17edbe038"
    PRI_KEY = "0000000xa036944e29568d0cff17edbe038" #private key

    # connect to the Tron blockchain
    client = Tron()
    recipient_address = 'TPhBQKb17edbe038f81208fecf9a66besaYutkvHqeWS'
    amount = 55000000

    Bl = Mining(account_ADDRESS,PRI_KEY)
    client=Bl.connection(recipient_address, amount)
    start = time.time()

    print("start  mining")
    print("-----------------------------------------------------")
    transaction = Check_valid("pug")
    new_hash = transaction.transaction(5,transactions,'17edbe038f81208fecf9a66be017edbe038f81208fecf9a66be9a2b8321c6ec7', level)
    total_time = str((time.time() - start))
    print("End mining.")
    print("-----------------------------------------------------")
    print(f" Mining took: {total_time} seconds")
    print("-----------------------New-Hash----------------------")
    print(new_hash)


