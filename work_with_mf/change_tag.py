import yaml

with open("mf", "a") as file:
  data_dict = yaml.dump(file)
  
  data_dict["image"] = "hello world!!!!!!"
  print(data_dict)
