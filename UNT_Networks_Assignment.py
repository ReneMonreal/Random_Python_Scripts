
import random

def NetworkSystem():
    Devices = [
        {"Name": "Router 1","Status": "Online","Mac Address": 1},
        {"Name": "Router 2","Status": "Offline","Mac Address": 2},
        {"Name": "Router 3","Status": "Online","Mac Address": 3},
        {"Name": "Router 4","Status": "Offline","Mac Address": 4}
    ]
    print(f'Current Devices: {Devices}')
    print('To send a message, type 1')
    print('To add a device, type 2')
    print('To delete a device, type 3')
    print('To update the status of your device, type 4')
    option = int(input("What would you like to do today? "))

    if option == 1:
        sender = input("What is your device name? ")
        #Find the sender device
        sender_device = None
        for device in Devices:
            if device["Name"] == sender:
                sender_device = device
                break
        if sender_device is None:
            print("Sender does not exist. Please enter a valid device or create a new one.")
            return
        
        reciver = input("Who would you like to send your message to? ")
        #Find the receiver device
        reciver_device = None
        for device in Devices:
            if device["Name"] == reciver:
                reciver_device = device
                break
        if reciver_device is None:
            print("Receiver device does not exist.")
            return
        if reciver_device["Status"].lower() == "offline":
            print("This device is offline and cannot receive messages.")
            return

        Ori_Packet = Create_Packet(sender, reciver)  
        print(f'Original Packet: {Ori_Packet}')     
        Shuf_Packet = ShufflePacket(Ori_Packet)
        print(f'Shuffled Packet: {Shuf_Packet}')
        print(f'Message has been sent to {reciver}')
        ReconstructedMessage = Reciving(Shuf_Packet, reciver, sender)
    elif option == 2:
        Device = input("What is the name of your device? ")
        print('Please enter either "Offline" or "Online"')
        Status = input("What is the Status of your device? ")
        if Status != "Offline" and Status != "Online":
            print('Invalid status. Please enter either "Offline" or "Online".')
        Devices = addDevice(Device, Status, Devices)
        print("Device has been added.")
        print(Devices)
    elif option == 3:
        selected_Removal = input("What device would you like to delete?: ")
        device_found = False
        for device in Devices:
            if device["Name"] == selected_Removal:
                Devices.remove(device) 
                device_found = True
                break
        
        if device_found:
            print(f"{selected_Removal} has been deleted.")
            print("Updated Devices:", Devices)
        else:
            print("Please enter a valid Device to delete.")
    elif option == 4:
        selected_Status = input("What device would you like to update the status of? ?: ")
        device_found = False
        for device in Devices:
            if device["Name"] == selected_Status:
                device_found = True
                break 
        if device_found == True:
            if device["Status"] == "Offline":
                device["Status"] == "Online"
            elif device["Status"] == "Online":
                device["Status"] == "Offline"
            print(f'Status updated to {device["Status"]}')
            print(Devices)
        else:
            print("Please enter a valid Device to update.")        

def Create_Packet(sender, reciver):
    message = input("What is your message? ")
    MessageLen = len(message)
    Ori_Packet = []
    for index, A in enumerate(message):
        packet = (MessageLen, index, A, sender, reciver)
        Ori_Packet.append(packet)
    return Ori_Packet

def ShufflePacket(Ori_Packet):
    Shuf_Packet = Ori_Packet.copy()
    random.shuffle(Shuf_Packet)
    return Shuf_Packet

def Reciving(Shuf_Packet, reciver, sender):
    print(f'202 Accepted by {reciver}')
    ReconstructedMessage = Reconstruct(Shuf_Packet)
    print(f'From {sender} To {reciver}: {ReconstructedMessage}')

def Reconstruct(Shuf_Packet):
    Original_Len = Shuf_Packet[0][0]
    ReconstructedMessage = [""] * Original_Len
    for packet in Shuf_Packet:
        _, index, A, sender, reciver = packet
        ReconstructedMessage[index] = A
    return "".join(ReconstructedMessage)

def addDevice(Device, Status, Devices):
    LenCurDevices = len(Devices)
    mac_counter = 1 + LenCurDevices
    Device_info = {
        "Name": Device,
        "Status": Status,
        "Mac Address": mac_counter
    }
    Devices.append(Device_info)
    return Devices

if __name__ == "__main__":
    NetworkSystem()
