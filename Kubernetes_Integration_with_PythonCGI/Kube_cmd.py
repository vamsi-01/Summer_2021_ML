#!/usr/bin/python3

print("content-type: text/html")
print()



import cgi,subprocess 

data =cgi.FieldStorage()
cmd = data.getvalue("command")
out=subprocess.getoutput("sudo "+cmd+" --kubeconfig /root/admin.conf")
print(out)
