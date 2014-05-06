score = raw_input('enter score:')
score = float(score)
try :
    

	if score >1:
		print 'please input a value between 0 and 1.0'
		quit()

	elif score <0 :
		print 'please input a value between 0 and 1.0'
		quit()
	elif score >= 0.9 :
		print 'A'
	elif score >= 0.8 :
		print 'B'
	elif score >= 0.7 :
		print 'C'
	elif score >= 0.6 :
		print 'D'
	elif score < 0.6 :
	    print 'F'
except:
    print 'enter numeric input'