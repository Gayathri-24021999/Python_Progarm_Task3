def write_to_file(file_name,content):
   with open(file_name, 'w') as file:
       file.write(content)
   print(f"Written to {file_name}")


file_name = 'example.txt'
initial_content = "Hi, I am gayathri."


write_to_file(file_name,initial_content)
