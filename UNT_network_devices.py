#The DataSet information is not real, info was selcted at random.

"""
Activity ONE: Build Your Own List of Devices
"""
my_devices = []
my_devices.extend([
    {'DeviceName': "Rene's Iphone", 'Status': False, 'IP_Address': '192.242.424.23', 'Model': 'Iphone 16 Pro Max 128 GB', 'Color': 'Space Grey'},
    {'DeviceName': "Rene's Mac", 'Status': True, 'IP_Address': '192.232.234.94', 'Model': 'Macbook Pro 16"', 'Color': 'Space Grey'},
    {'DeviceName': "Rene's Airpod Pros", 'Status': False, 'IP_Address': '192.245.374.236', 'Model': 'AirPods Pro 2"', 'Color': 'White'},
    {'DeviceName': "Rene's Apple Watch", 'Status': True, 'IP_Address': '192.323.545.68', 'Model': 'Series 10"', 'Color': 'Matte Green'},
    {'DeviceName': "Rene's Apple TV", 'Status': False, 'IP_Address': '192.543.469.57', 'Model': 'Apple TV 4K (3rd Generation) Wi-Fi + Ethernet"', 'Color': 'N/A'},
])




"""
Activity TWO: Bulk Status Update
Print your list to check each device’s status.
Update the status of all devices to either "active" or "maintenance".
Print again to confirm the update.
"""
for device in my_devices:
  print(device)
for device in my_devices:
  original = device['Status']
  if original == True: device['Status'] = "Active"
  elif original == False: device['Status'] = "Maintenance"
  else: print("Status Error")
for device in my_devices:
  print(f'{device["DeviceName"]} ---> Original Status Was "{original}" - New Status Is "{device["Status"]}"')
print()




"""
Activity THREE: Add/Remove Attributes
Add a new attribute to one dictionary (e.g., "ip_address" or "location").
Remove an existing attribute (e.g., "mac_address") from another dictionary.
Print your list again to confirm the changes.
  """
  #my_devices[4] is the location of the DataSet with the name "Rene's Apple TV"
my_devices[4].update({"Subscripton": True})
del my_devices[4]['Color']
for device in my_devices:
  print(device)
print()




"""
Activity: Filtering
Create a new list that filters devices by a certain criterion (e.g., status == "active").
Print out your filtered list to see the result.
"""
FilteredDevices = []
for device in my_devices:
  if device["Status"] == "Active":
    FilteredDevices.append(device)
print("The following devices are currently active")
for device in FilteredDevices:
  print(device)
print()
