import yaml
import sys

version = sys.argv[1]

with open('../../manifest/mf') as file:
  data_dict = yaml.load(file)
  
  data_dict['spec']['template']['spec']['containers'][0]['image'] = version
  
  with open('../../manifest/mf', 'w') as f:
        yaml.dump(data_dict, f)
    
