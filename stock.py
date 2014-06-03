import datetime
import sys
import executor



def execute(stockId=None, date=None):

	now = datetime.datetime.now()
	if date is None or len(date)==0:
        	#convert western calendar to R.O.C calendar
		date = str(now.year-1911) + "{:02d}".format(now.month) + "{:02d}".format(now.day)
	elif len(date)==4:
		date = str(now.year-1911) + date[0:2] + date[2:4]

	executor.execute(stockId, date)



if __name__ == "__main__":
	if len(sys.argv)<2:
		print 'Please input the stock id'
		exit()
	else:
		# TODO: check if the stock id is a valid one from some pre-defined stock list
		stockId = sys.argv[1]	
		if not stockId.isdigit():
			print "Please input a valid stock number as first argument"
			exit()
			
		if len(sys.argv)>2:
			date = sys.argv[2]
		else: 
			date = ''

		if len(date)!=4 and len(date)!=7 and len(date)!=0:
			print "Please input 4 or 7 numbers as date (ex: 0520, or 1030520)"
			exit() 
		
		execute(stockId, date)
		
   		
