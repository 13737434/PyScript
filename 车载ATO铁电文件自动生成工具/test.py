import base64
open_icon = open("photo.jpg","rb")
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = "img = '%s'" % b64str
f = open("photo.py","w+")
f.write(write_data)
f.close()