def eval_expr(vyraz,d={}):
	s = []
	vyraz=vyraz.split()
	n=len(vyraz)    
    
	for prvok in n:
		if vyraz[prvok] in d:
			s.append(int(d[vyraz[prvok]]))
    	if vyraz[prvok].isdigit():
    		s.append(int(vyraz[prvok])) 
    		s.append(int(d[vyraz[prvok]]))
    	if vyraz[prvok].isdigit():
    		s.append(int(vyraz[prvok]))    
		elif vyraz[prvok]=='+':
        	p1=s.pop()
        	p2=s.pop()
        	s.append(int(p1)+int(p2))
		elif vyraz[prvok]=='-':
        	p1=s.pop()
        	p2=s.pop()
        	s.append(int(p1)-int(p2))	
        elif vyraz[prvok]=='*':
        	p1=s.pop()
        	p2=s.pop()
        	s.append(int(p1)*int(p2))
		elif vyraz[prvok]=='/':
        	p1=s.pop()
        	p2=s.pop()
        	s.append(int(p1)/int(p2))
	return s.pop()
