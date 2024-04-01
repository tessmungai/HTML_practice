file_handle = open('myfile.txt','r')
for content in file_handle:
    print(content)
    
file_handle = open('myfile.txt','w')
file_handle.write("this message is new")
file_handle.close

file_handle = open('myfile.txt','a')
file_handle.write("this message has been appended")
file_handle.close

with open("myfile.txt", "r") as file:
      	content = file.read()
FileNotFoundError:[ Errno 2 ] No such file or directory: 'myfile.txt'


  
