from mininet.node import CPULimitedHost
from mininet.link import TCLink
...
net = Mininet( controller=Controller, host = CPULimitedHost, link = TCLink )

