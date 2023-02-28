s = '["python", "django"]'

result = s.strip('[]').replace("'", "").replace('"', '').split(',')
print(result, type(result))