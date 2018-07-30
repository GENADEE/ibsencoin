Ibsen Coin

IbsenCoin (IbC) is a cryptocurrency (duh) for fun(gibility). 

Design:
- IbsenCoin uses RSA blind signing to preserve anonymity and fungibility. 
  - IbsenCoins are transferred by being reminted into new IbsenCoins under the control of the new owner. 
  - IbsenCoins are reminted in batches. Remint orders for all new coins are signed by all old coins in the batch, so it is impossible to tell which coin they came from. 

Dependencies:

| pip install rsa

Transaction format:

- Once a sender has found a group of n senders each sending value v, each sender creates a transaction, which lists the inputs of all of the senders, the values of n and v, and the outputs for this particular sender, along with a timestamp at which the transaction expires. 
- Each sender then blinds his transaction using RSA encryption and sends their blinded transactions to all the other senders. 
- Each sender signs each of the blinded transactions he receives using the private keys associated with the inputs he controls, and sends the blind signatures back to the original sender. 
- Each sender then unblinds all the signatures for his transaction. He appends the signatures to the end of his transaction ordered by the values of the public keys associated with those signatures. 
- Each sender then sends his signed transaction to a node, hopefully masking his IP using onion or garlic routing. 
- Nodes relay transactions to each other. 
- A node confirms a transaction is valid if: the node has n different transactions from the same input, all unexpired, signed by all of the inputs, and with total output value of v, where all the inputs are valid and unspent, and the total value of the inputs > n * v. The node groups them into one transaction and adds it to the blockchain.
