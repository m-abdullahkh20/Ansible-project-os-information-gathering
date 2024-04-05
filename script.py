import os
import csv
import json
jsonfile='os_comands.json'
with open(jsonfile) as jf:
    my_dict=json.load(jf)

os_name=os.popen(my_dict['os_flavour']).read()

print(os_name)

if os_name == 'ubuntu' or os_name == 'centos':
    print("OS_FLAVOUR found plz wait to gather fuuther information!!!!")

    hostname=os.popen(my_dict['hostname']).read()
    print(hostname)
    
    ip=os.popen(my_dict['ip_qddress']).read()
    print(ip)
    
    df_details=os.popen(my_dict['df_data']).read()
    print(df_details)
    
    header_para=os.popen(my_dict['header_para']).read()
    print(header_para)

    data_csv = [hostname,ip,df_details]
    file1=open(r'/home/admin1/data_csv','a+')
    writer=csv.writer(file1)
    writer.writerow([header_para])
    writer.writerow([data_csv])
    file1.close()

    print("File imported successfully!!!!!!!!!!!!!")

else:
    print('Sorry!! OS not Found' )

