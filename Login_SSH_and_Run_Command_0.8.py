# coding=utf-8
#!/usr/bin/python 
import paramiko
import threading
from sys import argv
from os.path import exists #used for checking file in parameters
script, file1, input_cmd = argv 

def	ssh2(ip,username,passwd,cmd):
	try:
		ssh= paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip,22,username,passwd,timeout=5)
		for m in cmd:
			stdin, stdout, stderr = ssh.exec_command(m)
#           stdin.write("Yes")   #interaction here we input ‘Yes’ 
			out = stdout.readlines()
			#output to screen
			for o in out:
				print o,
		print '%s\tOK\n'%(ip)
		ssh.close()
	except :
		print '%s\tError\n'%(ip)

if __name__=='__main__':
	list=[]
	list.append(input_cmd)
	cmd = list#convert the string value to list
	in_file= open(file1)
	data = []
	for line in in_file:
		parameters = line.split()
		data.append(parameters)
	draw = len(data)
	threads = []
	print "There are %s devices"%(draw)
	print "Loading the configure file %s" %(file1)
	for i in range(draw):
		ip = data[i][0]
		username = data[i][1]
		passwd = data [i][2]
		a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
		a.start()

in_file.close()