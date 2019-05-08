import random
import numpy as np


# function to calculate the normal distribution
def calculation(height):

    height_target = height
    std = 1
    array_size = 40
    gaussian = np.random.normal(loc=height_target, scale=std, size=array_size)
    gaussian_info = ('the median height is {}, the standard deviation is {}, and the array size is {}'.format(height_target,std,array_size))
    print('calculando o desvio padrão')
    print(gaussian_info)
    return gaussian

# function to write the node file
def drone_node(coord, height):
    gaussian = calculation(height)
    # list of nodes id
    id_list = []
    node_id = -1
    nodes = (len(coord))
    # variable to access the coordinate element
    element = 0
    loop = 1
    # node file name
    print('escrevendo arquivos de nodes')
    nou = open('drone.nod.xml', 'w')
    nou.write('<?xml version="1.0" encoding="UTF-8"?> \n' '<nodes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/nodes_file.xsd"> \n')
    while loop <= nodes/2:
        coordx = coord[element]
        coordy = coord[element+1]
        coordz = random.choice(gaussian)
        node_id += 1
        id_list.append(node_id)
        element += 2
        loop += 1
        nou.write(('   <node id="d{}" x="{}" y="{}" z="{}"/> \n'.format(node_id, coordx, coordy, coordz)))
    nou.write('</nodes>')
    return id_list

def drone_edge(coord, height):
    id_list = drone_node(coord, height)
    print('escrevendo arquivos de edges')
    ed = open('drone.edg.xml', 'w')
    edges = (len(id_list))
    edge_loop = 0
    routes = []
    edge_id = -1
    element = 0
    ed.write(
        '<edges xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/edges_file.xsd"> \n')
    while edge_loop < edges:
        edge_id += 1
        departure = id_list[element]
        arrival = id_list[element + 1]
        element += 2
        edge_loop += 2
        # repeat the id for drone to come and go in the same lane
        ed.write(('   <edge id="dr{}" from="d{}" to="d{}" numLanes="1" priority="1"/> \n'.format(edge_id, arrival, departure)))
        routes.append(edge_id)
        edge_id += 1
        routes.append(edge_id)
        ed.write(('   <edge id="dr{}" from="d{}" to="d{}" numLanes="1" priority="1"/> \n'.format(edge_id, departure, arrival)))
    ed.write('</edges>')
    return (routes)


def drone_routes(routes):
    print(routes)
    rou = open('drone.rou.xml', 'w')
    rou.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    rou.write('<routes>\n')
    rou.write('  <vTypeDistribution id="typeDroneDistribution">\n')
    # drone model
    rou.write('        <vType id="Maverick" departSpeed="max" accel="2.0" decel="4.5" length="0.520" width="0.455" height="0.295" maxSpeed="20" speedDev="0.1" sigma="0.2" minGap="0.3" probability="1.0"/>\n')
    rou.write('  </vTypeDistribution>\n')
    route_number = (len(routes))
    start = 0
    time = 5000
    while start < route_number:
        rou.write(('      <flow id="dflow{}" color="0,0,1" begin="0" end= "{}" probability="0.03"  type="typeDroneDistribution">\n').format(routes[start], time))
        rou.write(('          <route edges="dr{}"/>\n').format(start))
        rou.write('      </flow>\n')
        start += 1
    rou.write('</routes>')
