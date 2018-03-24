import yaml
l = list(yaml.safe_load_all(open('config.yml','rb')))
print(l[0].get('URL'))