#gold standart reloaded
#how many bitcoins per capita after no more bitcoin will be mined in 2140

def max_bitcoins():
    
    #initial block reward of the genesis block was 50 BTC
    block_reward = 50
    # bitcoin halving after 210,000 blocks
    halving_interval = 210000
    
    total_bitcoin = 0
    while block_reward > 0:
        total_bitcoin += halving_interval * block_reward
        block_reward /= 2 
           
    return total_bitcoin

def coins_per_head():
    
    current_population = 7700000000
    per_capita = max_bitcoins()/current_population
    
    return per_capita

print('Number of Bitcoins to ever be in circulation: {:,} BTC.'.format(max_bitcoins()))

print('That is {:3.4f} Coins per head.'.format(coins_per_head()))
