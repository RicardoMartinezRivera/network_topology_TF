from asyncio.subprocess import DEVNULL
import json
import classes as c

def main():
    dList = c.DevicesList()
    lList = c.LinkList()

    # Device #1
    DEVICE_R1 = c.Device("R1", float(90), int(2))
    # Device Enpoint #R1-R2
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R1")
    d.add_endpoint_uuid("R1-2")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R1.endPoint_add(d)
    # Device Endpoint #R1-R3
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R1")
    d.add_endpoint_uuid("R1-3")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R1.endPoint_add(d)
    # Device Endpoint #R1-R4
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R1")
    d.add_endpoint_uuid("R1-4")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R1.endPoint_add(d)

    # Device #2
    DEVICE_R2 = c.Device("R2", float(90), int(2))
    # Device Enpoint #R2-R1
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R2")
    d.add_endpoint_uuid("R2-1")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R2.endPoint_add(d)
    # Device Endpoint #R2-R4
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R2")
    d.add_endpoint_uuid("R2-4")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R2.endPoint_add(d)

    # Device #3
    DEVICE_R3 = c.Device("R3", float(90), int(2))
    # Device Enpoint #R3-R1
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R3")
    d.add_endpoint_uuid("R3-1")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R3.endPoint_add(d)
    # Device Endpoint #R3-R4
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R3")
    d.add_endpoint_uuid("R3-4")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R3.endPoint_add(d)
    # Device Endpoint #R3-R5
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R3")
    d.add_endpoint_uuid("R3-5")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R3.endPoint_add(d)

    # Device #4
    DEVICE_R4 = c.Device("R4", float(90), int(2))
    # Device Enpoint #R4-R1
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R4")
    d.add_endpoint_uuid("R4-1")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R4.endPoint_add(d)
    # Device Endpoint #R4-R3
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R4")
    d.add_endpoint_uuid("R4-3")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R4.endPoint_add(d)
    # Device Endpoint #R4-R5
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R4")
    d.add_endpoint_uuid("R4-5")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R4.endPoint_add(d)
    # Device Endpoint #R4-R2
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R4")
    d.add_endpoint_uuid("R4-2")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R4.endPoint_add(d)
    
     # Device #5
    DEVICE_R5 = c.Device("R5", float(90), int(2))
    # Device Enpoint #R5-R3
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R5")
    d.add_endpoint_uuid("R5-3")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R5.endPoint_add(d)
    # Device Endpoint #R5-R4
    d = c.device_endpoint()
    d.add_topology_id("b55a05a5-ae2d-4ff3-85ca-97fac0c56f9", "abf65601-a36b-496f-8e21-1708e5f96e2d") 
    d.add_device_id("R5")
    d.add_endpoint_uuid("R5-4")
    d.add_endpoint_type("termination")
    d.add_direction_state(0, 0, 4)
    d.add_capacity_features(200, 200, 5)
    DEVICE_R5.endPoint_add(d)

    # Add Devices to the list
    dList.add(DEVICE_R1)
    dList.add(DEVICE_R2)
    dList.add(DEVICE_R3)
    dList.add(DEVICE_R4)
    dList.add(DEVICE_R5)

    # Link R1-R2
    LINK_R1_R2 = c.Link("R1-R2-LINK", float(0.6), int(2))
    print(LINK_R1_R2)



    # Add Links to the list
    lList.add(LINK_R1_R2)    
    
    with open('topology.json', 'w') as f:
        f.write(json.dumps({
            "deviceList": dList.to_json(),
            "linkList": lList.to_json()
            },indent=4))

if __name__ == '__main__':
    main()
