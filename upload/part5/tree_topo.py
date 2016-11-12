#!/usr/bin/env python
# sudo mn --custom tree_topo.py --topo AssignmentNetworks
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.log import setLogLevel


class AssignmentNetworks(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)

        lvl1_bw = 100
        lvl2_bw = 40
        lvl3_bw = 10

        lvl1_delay = '30ms'
        lvl2_delay = '20ms'
        lvl3_delay = '10ms'

        lvl1params = dict(bw=lvl1_bw, delay=lvl1_delay)
        lvl2params = dict(bw=lvl2_bw, delay=lvl2_delay)
        lvl3params = dict(bw=lvl3_bw, delay=lvl3_delay)


        #Start to build the tree here.

        # add switches
        c1 = self.addSwitch('c1')
        a1 = self.addSwitch('a1')
        a2 = self.addSwitch('a2')
        e1 = self.addSwitch('e1')
        e2 = self.addSwitch('e2')
        e3 = self.addSwitch('e3')
        e4 = self.addSwitch('e4')

        # add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')

        # create links
        self.addLink(c1, a1, **lvl1params)
        self.addLink(c1, a2, **lvl1params)
        self.addLink(a1, e1, **lvl2params)
        self.addLink(a1, e2, **lvl2params)
        self.addLink(a2, e3, **lvl2params)
        self.addLink(a2, e4, **lvl2params)
        self.addLink(e1, h1, **lvl3params)
        self.addLink(e1, h2, **lvl3params)
        self.addLink(e2, h3, **lvl3params)
        self.addLink(e2, h4, **lvl3params)
        self.addLink(e3, h5, **lvl3params)
        self.addLink(e3, h6, **lvl3params)
        self.addLink(e4, h7, **lvl3params)
        self.addLink(e4, h8, **lvl3params)

#if __name__ == '__main__':
setLogLevel( 'info' )

print("creating topology")
topo = AssignmentNetworks()

print("creating network")
net = Mininet(topo=topo, link=TCLink, autoSetMacs=True,
       autoStaticArp=True)

# Run network
print("starting network")
net.start()
# CLI( net )
net.pingAll()
net.stop()
