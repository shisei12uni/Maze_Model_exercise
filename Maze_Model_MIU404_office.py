office_for_MIU404 = {
    "office": {
     "capacity": 6,
     "residents": ["Shima", "Ibuki", "Kokonoe"],
     "directions": {"upstairs" : "kitchen",
                    "left" : "lockers",
                    "right" : "toilet"}
    },
    
    "kitchen": {
     "capacity": 1,
     "residents" : ["Jimba"],
     "directions" : {"downstairs": "office",
                     "jump": "office"}
    },
    
    "toilet": {
     "capacity": 1,
     "residents": [],
     "directions": {"left": "office"},
    },

    "lockers" :{
     "capacity": 4,
     "residents": ["Kikyou"],
     "directions": {"right": "office"},
    }
}

"""
#print (office_for_MIU404.keys()),
#print (office_for_MIU404.values())
print ("Mameji" in office_for_MIU404)

people_so_far = 0
total_capacity = 0

for rooms in office_for_MIU404:
    people_so_far = people_so_far + len(office_for_MIU404[rooms]["residents"])
    # print(len(office_for_MIU404[rooms]["residents"])) #check individual rooms
print(people_so_far)

for rooms in office_for_MIU404:
    total_capacity = total_capacity + office_for_MIU404[rooms]["capacity"]
    # print(office_for_MIU404[rooms]["capacity"]) #if it's numbers don't need to use len()
print(total_capacity)
"""

print({rooms: len(office_for_MIU404[rooms]["residents"]) 
       for rooms in office_for_MIU404
       if len(office_for_MIU404[rooms]["residents"] )})