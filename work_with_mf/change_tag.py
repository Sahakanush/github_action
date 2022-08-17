import yaml

with open("mf", "r") as file:
  data_dict = yaml.dump(file)
  
  data_dict["image"] = "hello world!!!!!!"
  print(data_dict)
