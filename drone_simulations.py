import os
import drone_sumo_files as we

# coord = [x1,y1,x2,y2,...,xn,yn] departure coordinate=(x1,y1) arrival coordinate=(x2,y2)
# sumo local coordinate
height = 50
coord = [-20.65, 109.59, 69.06, 131.69, 69.06, 131.69, 99.42, 249.66, -19.93, 69.83, 91.88, 319.33,
         69.06, 131.69, 132.32, 68.28, 69.06, 131.69, -20.79, 297.13, -32.93, 340.46, 106.69, 215.79]

routes = we.drone_edge(coord, height)
we.drone_routes(routes)

# call sumo command to generate a network
# os.system("netconvert --node-files=drone.nod.xml --edge-files=drone.edg.xml   --output-file=gaussian_drone.net.xml")
os.system("netconvert --sumo-net-file=seasonal.net.xml --node-files=drone.nod.xml --edge-files=drone.edg.xml   --output-file=gaussian_drone.net.xml")
