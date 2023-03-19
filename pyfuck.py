from string import ascii_lowercase
import sys

#returns the representation of a positive integer (>=0)
def number(n):
	if(n==0):
		return '+all([()])'
	return '+all([])'*n

#generates string representation from dictionary
def from_str(str_in):
	return "+".join([c[i] if i in c else from_ascii(i) for i in str_in])

#inserts chr() essentially
def from_ascii(n):
	return "eval("+from_str("chr("+str(ord(n))+")")+")"

#index generator
def ind(num):
	return "["+number(num)+"]"

#build up the decoding dict
true = "str(all([]))"
false = "str(all([()]))"
bset = "str(set([()]+[+all([])]))"

c = {}

#numbers
for i in range(10):
	c[str(i)] = "str("+number(i)+")"

#chars
c['('] = "str(())"+ind(0)
c[')'] = "str(())"+ind(1)
c['['] = "str([])"+ind(0)
c[']'] = "str([])"+ind(1)
c['{'] = bset+ind(0)
c['}'] = bset+ind(6)
c['<'] = "str(str)"+ind(0)
c['>'] = "str(str)"+ind(12)
c["'"] = "str(str)"+ind(7)
c['-'] = "str(eval)"+ind(6)
c[','] = "str([[]]+[()])"+ind(3)
c[' '] = "str([[]]+[()])"+ind(4)
c[':'] = "str(vars())"+ind(11)

#letters
c['a'] = false+ind(1)
c['b'] = "str(eval)"+ind(1)
c['c'] = "str(str)"+ind(1)
c['e'] = true+ind(3)
c['f'] = "str(eval)"+ind(10)
c['h'] = "str(vars(str))"+ind(str(vars(str)).index('h'))
c['i'] = "str(eval)"+ind(3)
c['j'] = "str(vars(str))"+ind(str(vars(str)).index('j'))
c['l'] = false+ind(2)
c['n'] = "str(eval)"+ind(12)
c['o'] = "str(eval)"+ind(16)
c['p'] = "str(vars(str))"+ind(str(vars(str)).index('p'))
c['r'] = true+ind(1)
c['s'] = "str(str)"+ind(4)
c['t'] = "str(str)"+ind(9)
c['u'] = true+ind(2)
c['v'] = "str(eval)"+ind(20)
c['w'] = "str(vars(str))"+ind(str(vars(str)).index('w'))

#SECOND ITERATION OF CHAR BUILDING
zdz = "eval("+from_str("str(float(0))")+")"
c['.'] = zdz+ind(1)

varl = "eval("+from_str("list(vars())")+")"
c['_'] = varl+ind(0)+ind(0)
c['d'] = varl+ind(1)+ind(2)
c['m'] = varl+ind(0)+ind(4)
c['g'] = varl+ind(2)+ind(7)
c['k'] = varl+ind(2)+ind(5)

def main():
	if(len(sys.argv) != 3):
		raise Exception("incorrect number of args provided")

	code = open(sys.argv[1], "r").read();
	code = code.replace("\\", R"\\")
	#code = code.replace(R'"\n"', "chr(10)")
	print(code)

	pyf = from_str(code)
	pyf = "eval("+from_str("exec('''")+"+"+pyf+"+"+from_str("''')")+")"
	print("wrote", open(sys.argv[2], "w").write(pyf), "chars")

if(__name__ == "__main__"):
	main()
