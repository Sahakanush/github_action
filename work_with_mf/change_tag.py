import yaml

with open('mf') as file:
  data_dict = yaml.load(file)
  print(data_dict)
  
  data_dict['spec']['template']['spec']['containers'][0]['image'] = "hello world!!!!!!"
  
  with open('mf', 'w') as f:
        yaml.dump(data_dict, f)
    
