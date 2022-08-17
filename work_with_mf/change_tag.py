import yaml

with open("mf", "r") as file:
  f_list = yaml.load(file, Loader=yaml.FullLoader)
  print(f_list)
