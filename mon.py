import os
import psutil
import platform

print()

def get_data():
    sensor_data = psutil.sensors_temperatures()
    cleaned_data = dict()

    # Machine Name
    cleaned_data['machine'] = platform.node()

    # Nvme
    cleaned_data['nvme'] = {'temp' : sensor_data['nvme'][0][1], 'temp_max' : sensor_data['nvme'][0][3]}

    # CPU
    cpu_freq = psutil.cpu_freq()
    cleaned_data['cpu'] = {'temp' : sensor_data['k10temp'][0][1],
                           'temp_max' : 100,
                           'clock' : cpu_freq[0],
                           'clock_min' : cpu_freq[1],
                           'clock_max' : cpu_freq[2],
                           'cores' : psutil.cpu_count(logical=False)}
    
    
    return cleaned_data
    
    


print(get_data())