import json

class device_endpoint():
    
    def __init__(self):
        pass

    def add_topology_id(self, topology_uuid, context_uuid):
        self.topology_uuid = topology_uuid
        self.context_uuid = context_uuid

    def add_device_id(self, device_id):
        self.device_id = device_id

    def add_endpoint_uuid(self, endpoint_uuid):
        self.endpoint_uuid = endpoint_uuid

    def add_endpoint_type(self, endpoint_type):
        self.add_endpoint_type = endpoint_type

    def add_direction_state(self, link_port_direction, termination_direction, termination_state):
        self.link_port_direction = link_port_direction
        self.termination_direction = termination_direction
        self.termination_state = termination_state

    def add_capacity_features(self, total, available, unit):
        self.unit = unit
        self.total_capacity = total
        self.available_capacity = available

    def to_json(self):
        return{"endpoint_id": {"topology_id": {"contextId": self.topology_uuid, 
                "topology_uuid": self.context_uuid},
                "device_id": self.device_id,
                "endpoint_uuid": self.endpoint_uuid},
                "endpoint_type": self.add_endpoint_type,
                "link_port_direction": self.link_port_direction,
                "termination-direction": self.termination_direction,
                "termination-state": self.termination_state,
                "total-potential-capacity": {"total-size": {"value": self.total_capacity, 
                "unit": self.unit}}, "available-capacity": {"total-size": {"value": self.available_capacity, 
                "unit": self.unit}}
                }

    
class Device():
    def __init__(self, device_id):
        self.device_id = device_id
        self.device_type = "L3"        
        self.device_endpoints = []
        self.power_idle = float(0)
        self.operational_status = int(0)

    def add_power_info(self, power_idle, operational_status):        
        self.power_idle = power_idle
        self.operational_status = operational_status

    def endPoint_add(self, device_endpoint):
        self.device_endpoints.append(device_endpoint)

    def getEndPoint(self, endPointId):
        for i,endP in enumerate(self.device_endpoints):
            if endP.endpoint_uuid == endPointId:
                return endP
        return None

    def __str__(self):
        return "{}".format(self.device_id)

    def __repr__(self) -> str:
        return "{}".format(self.device_id)
    
    def to_json(self):
        return {"device_id": self.device_id,
                "device_type": self.device_type,
                "power_idle": self.power_idle,
                "operational_status": self.operational_status,
                "device_endpoints": [device_endpoint.to_json() for device_endpoint in self.device_endpoints]
                }

class DevicesList:
    def __init__(self):
        self.devices = []

    def add(self, device):
        self.devices.append(device)

    def find(self, id):
        print("id: {}".format(str(id)))
        #print("Length Devices: {}".format(len(self.devices)))
        for i, d in enumerate(self.devices):
            print("[{}] -- deviceId: {}".format(i, d.device_id))
            if d.device_id == id:
                return i
        return -1

    def get(self, id):
        print("get device tied to id: {}".format(id))
        for i, d in enumerate(self.devices):
            if d.device_id == id:
                return d
        return None  
    
    def show(self):
        for d in self.devices:
            print("device {}".format(d.device_id))
    
    def to_json(self):
        return [device.to_json() for device in self.devices]   

class LinkEndpoint():
    def __init__(self, context_uuid, topology_uuid, deviceId, endPointId):
        self.context_uuid = context_uuid
        self.topology_uuid = topology_uuid
        self.deviceId = deviceId
        self.endPointId = endPointId

    def to_json(self):
        return {"endpoint_id": {"topology_id": {"contextId": self.context_uuid, "topology_uuid": self.topology_uuid},
               "device_id": self.deviceId, "endpoint_uuid": self.endPointId}        
        }

class Link():
    def __init__(self, link_Id, energy_link, operational_status, fwd_dir):
        self.link_Id = link_Id
        self.energy_link = energy_link
        self.operational_status = operational_status
        self.fwd_dir = fwd_dir
        self.linkEndPoints = []
        self.total_potential_capacity = float(0)
        self.available_capacity = float(0)
        self.unit = int(0)
        self.costName = ""
        self.costValue = float(0)
        self.costAlg = float(0)
        self.latency = float(0)

    def __repr__(self) -> str:
        return "{} {} {} {}".format(self.link_Id, self.energy_link, self.operational_status, self.fwd_dir)

    def add(self, linkEndpoint):
        self.linkEndPoints.append(linkEndpoint)

    def add_capacity(self, total, available, unit):
        self.total_potential_capacity = total
        self.available_capacity = available
        self.unit = unit

    def add_cost(self, costName, cost_value, cost_algorithm):
        self.costName = costName
        self.costValue = cost_value
        self.costAlg = cost_algorithm
    
    def add_latency(self, latency):
        self.latency = latency
    
    def to_json(self):
        return {"link_Id": self.link_Id,
                "energy_link": self.energy_link,
                "operational_status": self.operational_status,
                "link_endpoint_ids": [linkEndpoint.to_json() for linkEndpoint in self.linkEndPoints],
                "forwarding_direction": self.fwd_dir,
                "total-potential-capacity": {"total-size": {"value": self.total_potential_capacity, "unit": self.unit}}, 
                "available-capacity": {"total-size": {"value": self.available_capacity, "unit": self.unit}}, 
                "cost-characteristics": {"cost-name": self.costName, "cost-value": self.costValue, "cost-algorithm": self.costAlg},
                "latency_characteristics": {"fixed-latency-characteristics": self.latency}}
class LinkList():
    def __init__(self):
        self.links = []

    def add(self, link):
        self.links.append(link)

    def get(self, id):
        #print("Check if linkid: {} is on the link list".format(id))
        for l in self.links:
            if l.link_Id == id:
                return l
        return None

    def to_json(self):
        return[link.to_json() for link in self.links]

class ServiceId():
    def __init__(self, contextId, service_uuid):
        self.contextId = contextId
        self.service_uuid = service_uuid

    def to_json(self):
        return{"contexId": self.contextId,
                "service_uuid": self.service_uuid}

class ServiceEndpoint():
    def __init__(self):
        contextId = ""
        topology_uuid = ""
        device_id = ""
        endpoint_uuid = ""

    def add_context_topology(self, contextId, topology_uuid):
        self.contextId = contextId
        self.topology_uuid = topology_uuid

    def add_device_endpoint(self, device_id, endpoint_uuid):
        self.device_id = device_id
        self.endpoint_uuid = endpoint_uuid

    def to_json(self):
        return{"topology_id": {"contextId": self.contextId,
        "topology_uuid": self.topology_uuid}, "device_id": self.device_id, "endpoint_uuid": self.endpoint_uuid}

class Service(ServiceId):
    def __init__(self, contextId, service_uuid):
        super().__init__(contextId, service_uuid)
        self.algId = ""
        self.syncPaths = ""
        self.type = 0
        self.endpoints_ids = []
        self.bandwidth = 0.0
        self.latency = 0.0
        self.kpaths = 0

    def add_serv_att(self, algId, syncPaths, type):
        self.algId = algId
        self.syncPaths = syncPaths
        self.type = type

    def add_endpoint_id(self, serviceEndpoint):
        self.endpoints_ids.append(serviceEndpoint)

    def add_serv_args(self, bandwidth, latency, kpaths):
        self.bandwidth = bandwidth
        self.latency = latency
        self.kpaths = kpaths

    def to_json(self):
        return {"algId": self.algId, "syncPath": self.syncPaths,
                "serviceId": super().to_json(), "serviceType": self.type, 
                "service_endpoints_ids": [service_endpoint.to_json() for service_endpoint in self.endpoints_ids], 
                "service_constraints": [{"constraint_type": "bandwidth", "constraint_value": self.bandwidth}, 
                {"constraint_type": "latency", "constraint_value": self.latency}],
                "kPaths": self.kpaths}    

class ServiceList():
    def __init__(self):
        self.services = []
    
    def add(self, service):
        self.services.append(service)

    def get(self, id):
        for i,s in enumerate(self.services):
            if s.service_uuid == id:
                return s
        return None
    
    def to_json(self):
        return[service.to_json() for service in self.services]