import base64
open_icon = open("Model.docx","rb")
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = "docx = '%s'" % b64str
f = open("model.py","w+")
f.write(write_data)
f.close()