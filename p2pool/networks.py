from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    qcoin=math.Object(
        PARENT=networks.nets['qcoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='fc70035c7a81bc6f'.decode('hex'),
        PREFIX='2472ef181efcd37b'.decode('hex'),
        P2P_PORT=8883,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=8888,
        BOOTSTRAP_ADDRS='tata.wonabru.com brat.wonabru.com wonabru.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool',
        VERSION_CHECK=lambda v: 160600 <= v < 160600 or 160600 <= v,
        VERSION_WARNING=lambda v: 'Upgrade Qcoin to >=1.6.6.6!' if v < 160600 else None,
    ),
    bitcoin_testnet=math.Object(
        PARENT=networks.nets['bitcoin_testnet'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=60*60//10, # shares
        REAL_CHAIN_LENGTH=60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='5fc2be2d4f0d6bfb'.decode('hex'),
        PREFIX='3f6057a15036f441'.decode('hex'),
        P2P_PORT=19333,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=19332,
        BOOTSTRAP_ADDRS='forre.st vps.forre.st liteco.in'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v,
    ),
    
    litecoin=math.Object(
        PARENT=networks.nets['litecoin'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='e037d5b8c6923410'.decode('hex'),
        PREFIX='7208c1a53ef629b0'.decode('hex'),
        P2P_PORT=9338,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=9327,
        BOOTSTRAP_ADDRS='forre.st vps.forre.st liteco.in 95.211.21.103 37.229.117.57 66.228.48.21 180.169.60.179 112.84.181.102 74.214.62.115 209.141.46.154 78.27.191.182 66.187.70.88 88.190.223.96 78.47.242.59 158.182.39.43 180.177.114.80 216.230.232.35 94.231.56.87 62.38.194.17 82.67.167.12 183.129.157.220 71.19.240.182 216.177.81.88 109.106.0.130 113.10.168.210 218.22.102.12 85.69.35.7:54396 201.52.162.167 95.66.173.110:8331 109.65.171.93 95.243.237.90 208.68.17.67 87.103.197.163 101.1.25.211 144.76.17.34 209.99.52.72 198.23.245.250 46.151.21.226 66.43.209.193 59.127.188.231 178.194.42.169 85.10.35.90 110.175.53.212 98.232.129.196 116.228.192.46 94.251.42.75 195.216.115.94 24.49.138.81 61.158.7.36 213.168.187.27 37.59.10.166 72.44.88.49 98.221.44.200 178.19.104.251 87.198.219.221 85.237.59.130:9310 218.16.251.86 151.236.11.119 94.23.215.27 60.190.203.228 176.31.208.222 46.163.105.201 198.84.186.74 199.175.50.102 188.142.102.15 202.191.108.46 125.65.108.19 15.185.107.232 108.161.131.248 188.116.33.39 78.142.148.62 69.42.217.130 213.110.14.23 185.10.51.18 74.71.113.207 77.89.41.253 69.171.153.219 58.210.42.10 174.107.165.198 50.53.105.6 116.213.73.50 83.150.90.211 210.28.136.11 86.58.41.122 70.63.34.88 78.155.217.76 68.193.128.182 198.199.73.40 193.6.148.18 188.177.188.189 83.109.6.82 204.10.105.113 64.91.214.180 46.4.74.44 98.234.11.149 71.189.207.226'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-ltc',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Litecoin to >=0.8.5.1!' if v < 80501 else None,
    ),
    litecoin_testnet=math.Object(
        PARENT=networks.nets['litecoin_testnet'],
        SHARE_PERIOD=4, # seconds
        CHAIN_LENGTH=20*60//3, # shares
        REAL_CHAIN_LENGTH=20*60//3, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='cca5e24ec6408b1e'.decode('hex'),
        PREFIX='ad9614f6466a39cf'.decode('hex'),
        P2P_PORT=19338,
        MIN_TARGET=2**256//50 - 1,
        MAX_TARGET=2**256//50 - 1,
        PERSIST=False,
        WORKER_PORT=19327,
        BOOTSTRAP_ADDRS='forre.st vps.forre.st'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),

    terracoin=math.Object(
        PARENT=networks.nets['terracoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//30, # shares
        REAL_CHAIN_LENGTH=24*60*60//30, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=15, # blocks
        IDENTIFIER='a41b2356a1b7d46e'.decode('hex'),
        PREFIX='5623b62178d2b9b3'.decode('hex'),
        P2P_PORT=9323,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=9322,
        BOOTSTRAP_ADDRS='seed1.p2pool.terracoin.org seed2.p2pool.terracoin.org forre.st vps.forre.st 93.97.192.93 66.90.73.83 67.83.108.0 219.84.64.174 24.167.17.248 109.74.195.142 83.211.86.49 94.23.34.145 168.7.116.243 94.174.40.189:9344 89.79.79.195 portals94.ns01.us'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: 80002 <= v,
        VERSION_WARNING=lambda v: 'Upgrade Terracoin to >= 0.8.0.2!' if v < 80002 else None,
    ),
    terracoin_testnet=math.Object(
        PARENT=networks.nets['terracoin_testnet'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=60*60//30, # shares
        REAL_CHAIN_LENGTH=60*60//30, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=15, # blocks
        IDENTIFIER='b41b2356a5b7d35d'.decode('hex'),
        PREFIX='1623b92172d2b8a2'.decode('hex'),
        P2P_PORT=19323,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=19322,
        BOOTSTRAP_ADDRS='seed1.p2pool.terracoin.org seed2.p2pool.terracoin.org forre.st vps.forre.st'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Terracoin to >= 0.8.0.1!' if v < 80001 else None,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
