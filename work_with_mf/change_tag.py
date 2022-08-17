import yaml

with open(r'manifest\mf') as file:
  f_list = yaml.load(file, Loader=yaml.FullLoader)
  print(f_list)
