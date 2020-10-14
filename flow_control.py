#define a subroutine 
def flow_control(k):

	#"defines a string based on the value of k" 
	#incorporates a string 

	if(k==0): # (k==0)|(k==5) | is or

		s="Variable k = %d equals 0." % k 
		# %d calls the variable at the end of the line

	elif(k==1):

		s="Variable k = %d equals 1." % k

	else: #for everything else

		s="Variable k = %d does not equal 1 or 0."

	print(s) #variable s is printed


def main():

	i = 0 #declares integer to pass to flowcontrol

	flow_control(i) #passing integer

	