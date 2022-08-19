import yaml
import sys

version = sys.argv[1]

with open('/home/runner/work/testingInfra/WebApps/identidockui.yaml ') as file:
  data_dict = yaml.load(file)
  
  data_dict['spec']['template']['spec']['containers'][0]['image'] = version
  
  with open('/home/runner/work/testingInfra/WebApps/identidockui.yaml', 'w') as f:
        yaml.dump(data_dict, f)
    
