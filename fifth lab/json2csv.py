def task4():
    import json
    import pandas
    name = input()
    with open(name, 'r') as j:
        js_data = json.loads(j.read())
        
    json_data = pandas.DataFrame(js_data)
    json_data.to_csv(name[:-4]+'.csv',index=False)
task4()