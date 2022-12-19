import os
import sys
import classes as c
import json


# Creating the list of the Devices
dList = c.DevicesList()
# Creating the list of Links
lList = c.LinkList()
# service List 
sList = c.ServiceList()

def process_devices(cmd):
    num_devices = int(cmd[1]) #the number of devices is indicated in c[1]
    #print("Num devices: {}".format(num_devices))
    # Allocate each individual device
    for i in range(num_devices):
        print("Add Device with Id: {}".format(str(cmd[i+2])))
        d = c.Device(str(cmd[i+2]))
        dList.add(d)
    return

def format_device(cmd):
    # get the device cmd[1] in dList
    i = dList.find(str(cmd[1]))
    if i < 0:
        print("Device Id: {} NOT FOUND... weird".format(str(cmd[1])))
        sys.exit()
    else:
        print("Device Id: {} FOUND @ [{}]".format(str(cmd[1]), i))
        # Store the power_idle (cmd[3]) and operational status (cmd[5])        
        for j,d in enumerate(dList.devices):
            if i == j:
                d.add_power_info(float(cmd[3]), int(cmd[5]))
                break
def device_endpoint(cmd):
    # find the device specified in cmd[1]
    #print("Associated Device Id: {}".format(str(cmd[1])))
    d = dList.get(str(cmd[1]))
    if d == None:
        print("Device Id: {} NOT FOUND... weird".format(str(cmd[1])))
        sys.exit()
    else:
        print("Device Id: {} FOUND".format(d.device_id))
        dEndP = c.device_endpoint()
        dEndP.add_device_id(str(cmd[1]))
        dEndP.add_endpoint_uuid(str(cmd[2]))
        dEndP.add_topology_id(str(cmd[3]), str(cmd[4]))
        d.endPoint_add(dEndP)

def endpoint_attributes(cmd):
    # 1st retieves the Device by its ids from device list    
    d = dList.get(str(cmd[1]))
    if d == None:
        print("Device Id: {} NOT FOUNH... weirf".format(str(cmd[1])))
        sys.exit()
    # If found, then get the endpoint by its endpoint_id
    dEndP = d.getEndPoint(str(cmd[2]))
    if dEndP == None:
        print("Device EndPoint: {} NOT FOUNH... weirf".format(str(cmd[2])))
        sys.exit()
    #print("Device: {} and EndpointUUID: {} is FOUND".format(d.device_id, dEndP.endpoint_uuid))
    dEndP.add_endpoint_type(str(cmd[3]))
    dEndP.add_direction_state(int(cmd[4]), int(cmd[5]), int(cmd[6]))    
    dEndP.add_capacity_features(float(cmd[8]), float(cmd[10]), float(cmd[12]))

def linkid_creation(cmd):
    # 1st retrieves the Link by its ids from link list. If 
    # it is not found, create it; otherwise, inform that linkid already exists
    l = lList.get(str(cmd[1]))
    if l == None:
        link = c.Link(str(cmd[1]), float(cmd[3]), int(cmd[5]), int(cmd[7]))
        lList.add(link)
        print("{} link is ADDED".format(str(cmd[1])))
    else:
        print("LinkId {} already exists ...".format(str(cmd[1])))
        pass

def link_endpoint_add(cmd):
    # get the link by its id; if it does not exist, ignore the command
    l = lList.get(cmd[1])
    if l == None:
        print("LinkId: {} DOES NOT EXIST...".format(cmd[1]))
    else:
       print("LinkId: {} FOUND".format(l.link_Id))
       linkEndpoint = c.LinkEndpoint(str(cmd[2]), str(cmd[3]), str(cmd[4]), str(cmd[5]))
       l.add(linkEndpoint)

def link_capacity_add(cmd):
    # get the link by its id; if it does not exist, ignore the command
    l = lList.get(cmd[1])
    if l == None:
        print("LinkId: {} DOES NOT EXIST...".format(cmd[1]))
    else:
        l.add_capacity(float(cmd[3]), float(cmd[5]), int(cmd[7]))

def  link_cost_add(cmd):
    # get the link by its id; if it does not exist, ignore the command
    l = lList.get(cmd[1])
    if l == None:
        print("LinkId: {} DOES NOT EXIST...".format(cmd[1]))
    else:
        l.add_cost(str(cmd[3]), float(cmd[5]), float(cmd[7]))

def link_latency_add(cmd):
    # get the link by its id; if it does not exist, then ignore the command
    l = lList.get(cmd[1])
    if l == None:
        print("LinkId: {} DOES NOT EXIST...".format(cmd[1]))
    else:
        l.add_latency(str(cmd[2]))

def add_service_att(cmd):
    s = sList.get(str(cmd[1]))
    if s == None:
        print("service with id: {} NOT found".format(str(cmd[1])))
        sys.exit()
    else:
        s.add_serv_att(str(cmd[3]), str(cmd[5]), int(cmd[7]))

def service_endpoint_add(cmd):
    s = sList.get(str(cmd[1]))
    if s == None:
        print("Service_id: {} is NOT found".format(str(cmd[1])))
    else:
        endpointId = c.ServiceEndpoint()
        endpointId.add_context_topology(str(cmd[3]), str(cmd[5]))
        endpointId.add_device_endpoint(str(cmd[7]), str(cmd[9]))
        s.add_endpoint_id(endpointId)
def service_args_add(cmd):
    s = sList.get(str(cmd[1]))
    if s == None:
        print("Service_id: {} is NOT found".format(str(cmd[1])))
    else:
        print("bandwidth: {}; latency: {}, kPaths: {}".format(float(cmd[3]), float(cmd[5]), int(cmd[7])))
        s.add_serv_args(float(cmd[3]), float(cmd[5]), int(cmd[7]))        

def process_line(l):
    cmd = l.split()
    if cmd[0] == "#":
        pass
    elif cmd[0] == "devices":
        print("{}".format(cmd[0]))
        process_devices(cmd)
    
    elif cmd[0] == "device":
        format_device(cmd)

    elif cmd[0] == "device_endpoint":
        device_endpoint(cmd)

    elif cmd[0] == "endpoint_att":
        endpoint_attributes(cmd)
    
    elif cmd[0] == "linkid":
        linkid_creation(cmd)

    elif cmd[0] == "link_endpoint":
        link_endpoint_add(cmd)

    elif cmd[0] == "link_capacity":
        link_capacity_add(cmd)

    elif cmd[0] == "link_cost":
        link_cost_add(cmd)
    
    elif cmd[0] == "link_latency":
        link_latency_add(cmd)

    elif cmd[0] == "service":
        sId = c.ServiceId(str(cmd[2]), str(cmd[4]))
        #append the service
        s = c.Service(sId.contextId, sId.service_uuid)
        sList.add(s)
    elif cmd[0] == "serviceAtts":
        add_service_att(cmd)
    elif cmd[0] == "serviceEndPoint":
        service_endpoint_add(cmd)
    elif cmd[0] == "serviceArgs":
        service_args_add(cmd)
    else:
        print("Command: {} NOT KNOWN".format(cmd[0]))
        pass


def main():
    # cwd = os.getcwd()
    # files = os.listdir(cwd)
    # print("Files in %r: %s" % (cwd, files))
    
    
    with open("infra.txt", "r") as f:
        lines = [line.rstrip() for line in f]
    
    print(lines)

    for line in lines:
        process_line(line)

    # Creating the topology.json
    with open('topology.json', 'w') as f:
        f.write(json.dumps({
            "serviceList":sList.to_json(),
            "deviceList": dList.to_json(),
            "linkList": lList.to_json()            
            },indent=4))
    print("Devices Length: {}; LinkList Length: {}".format(len(dList.devices), len(lList.links)))

if __name__ == '__main__':
    main()