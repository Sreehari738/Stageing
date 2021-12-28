class student:
	def getstudent(self):
		self.sid=int(input("enter student id:"))
		self.sname=input("enter student name:")
		self.maths=int(input("enter student maths marks:"))
		self.physics=int(input("enter student physics marks:"))
		self.chemistry=int(input("enter student chemistry marks:"))
		self.english=int(input("enter student english marks:"))
		self.social=int(input("enter student social marks:"))
		self.computer=int(input("enter student computer marks:"))
		self.total=0
		self.avg=0
		self.grade=""	
			
	def lastname(self):
		return(self.sname.split()[-1])
	def findstudenttotalmarks(self):
		self.total=(self.maths+self.physics+self.chemistry+self.english+self.social+self.computer)
		self.avg=self.total/6
		if(self.maths<35 or self.physics<35 or self.chemistry<35 or self.english<35 or self.social<35 or self.computer<35):
			self.grade='Fail'	
		elif(self.avg>=90):
			self.grade=='A+'
		elif(self.avg>=80):		
			self.grade='A'
		elif(self.avg>=70):
			self.grade='B'
		elif(self.avg>=50):
			self.grade='C'
		elif(self.avg>=35):
			self.grade='D'
		

	def displaystudent(self):
		print("student id:",self.sid)
		print("student name:",self.sname)
		print("student maths:",self.maths)
		print("student physics:",self.physics)
		print("student chemistry:",self.chemistry)
		print("student english:",self.english)
		print("student social:",self.social)
		print("student computer:",self.computer)
		print("student total marks:",self.total)
		print("student avg marks:",self.avg)
		print("student grade:",self.grade)
		
	
if __name__=='__main__':
	s1=student()	
	s2=student()
	s1.getstudent()
	s2.getstudent()
	print(s1.lastname(),s2.lastname())
	s1.findstudenttotalmarks()
	s2.findstudenttotalmarks()
	s1.displaystudent()


	#s3.displaystudent()
	
	
	
	

	
