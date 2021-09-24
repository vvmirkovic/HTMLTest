import json

req_services = ["EC2AllowedActions", "EKSAllowedActions"]
a = {1:1,2:2}
print(a.keys())
#Open json file and convert it to a dictionary
with open("fakepolicies.json") as f:
    general_document = json.load(f)
    all_services = general_document["Statement"]
    
    ### add services from all_services to selected services only if it is listed in req_services
    selected_services = [x for x in all_services if x['Sid'] in req_services]


#    for service in all_services:
#        if service["Sid"] in req_services:
#            selected_services.append(service)


    
print( [x['Sid'] for x in selected_services] )
