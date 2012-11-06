import sys
import string

#first handle input parameter
if len(sys.argv) < 2:  
    print 'please input: --switch xx --host xx\n' 

for i in range(1,len(sys.argv[1:])+1):
    if sys.argv[i] == '--switch' or sys.argv[i] == '-s':
        switch = string.atoi(sys.argv[i+1])
    if sys.argv[i] == '--host' or sys.argv[i] == '-h':
        host = string.atoi(sys.argv[i+1])
print "host:", host, "switch:", switch

#then about file we gonna write
fileHandle = open ( 'newtopo.py', 'w' )
init = "from mininet.topo import Topo, Node\n\nclass MyTopo( Topo ):\
\n    def __init__( self, enable_all = True ):\n        super( \
MyTopo, self ).__init__()\n        # Set Node IDs for hosts and \
switches\n"

#now let's create file
fileHandle.write( init )
for i in range(1,host+1):
    hostn = '        Host' + str(i) + ' = ' + str(i) + '\n'
    fileHandle.write( hostn )
for i in range(host+1,switch+host+1):
    switchn = '        Switch' + str(i-host) + ' = ' + str(i) + '\n'
    fileHandle.write( switchn )

fileHandle.write( '\n' )
fileHandle.write( '        # Add nodes\n' )
#then write defination
for i in range(1,host+1):
    hostn = '        self.add_node( Host' + str(i) + ', Node( is_switch=False ) )\n'
    #print hostn
    fileHandle.write( hostn )
for i in range(1,switch+1):
    switchn = '        self.add_node( Switch' + str(i) + ', Node( is_switch=True ) )\n'
    #print switchn
    fileHandle.write( switchn )

#at last, create edge
fileHandle.write( '\n' )
fileHandle.write( '        # Add edge\n' )
for i in range(1,switch+1):
    link = '        self.add_edge( Switch' + str(i) + ', Switch' \
+ str(switch if i == switch-1 else (i+1)%switch) +' )\n'
    fileHandle.write( link )

for i in range(1,host+1):
    link = '        self.add_edge( Host' + str(i) + ', Switch' + \
str(switch if i%switch == 0 else i%switch) +' )\n'
    fileHandle.write( link )

fileHandle.write( "        self.enable_all()\n\n" )
fileHandle.write( "topos = { 'mytopo': ( lambda: MyTopo() ) }" )
