from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from pymongo import *
import matplotlib.pyplot as plt 
import numpy as np
import requests

def f1():
	root.withdraw()
	ae.deiconify()
def f2():
	root.withdraw()
	ve.deiconify()
	ve_st_data.delete(1.0,END)
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["EMS_11Jan"]
		coll=db["employee"]
		data=coll.find()
		info=""
		for d in data:
			info=info+"Id:"+str(d["_id"])+"name="+str(d["name"])+"sal:"+str(d["salary"])+"\n"
		ve_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

def f3():
	root.withdraw()
	ue.deiconify()
def f4():
	root.withdraw()
	de.deiconify()
def f5():
	root.withdraw()
	ce.deiconify()
def f6():
	ue.withdraw()
	root.deiconify()
def f7():
	de.withdraw()
	root.deiconify()
def f8():
	ae.withdraw()
	root.deiconify()
def f9():
	ve.withdraw()
	root.deiconify()
def f10():
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["EMS_11Jan"]
		coll=db["employee"]
		#-------validation for Id----------
		Id=ae_ent_id.get()
		if (Id == '' ):
			raise Exception("ID cannot be blank!")
		elif(not Id.lstrip("-").isdigit() and Id!=""):
			raise Exception("ID should only have numbers!")
		else:
			Id=int(Id)
			if(Id<0):
				raise Exception("Id cannot be less than zero!")
		#------validation for name-----------
		name=ae_ent_name.get()
		if(name==""):
			raise Exception("name cannot be empty!")
		elif(not name.isalpha()):
			raise Exception("Name should contain only letters!")
		elif(len(name)<2):
			raise Exception("Name should have minimum 2 alphabets!")
		#---------validtaion for salary--------
		salary=ae_ent_salary.get()
		if(salary==''):
			raise Exception("salary cannot be empty!")
		elif(not salary.isdigit() and salary!=""):
			raise Exception("salary must have only numbers!")
		else:
			salary=int(salary)
			if(salary<0):
				raise Exception("salary cannot be less than zero!")
			elif(salary<8000):
				raise Exception("salary should be more than 8000")
			
		count=coll.count_documents({"_id":Id})
		if count==1:
				# showinfo(Id,"Already Exists.")
				raise Exception("Already Exists")
		else:
					info={"_id":Id,"name":name,"salary":salary}
					coll.insert_one(info)
					showinfo("Success","Recored Created")

				
	except Exception as e:
		showerror("Khushi",e)
	finally:
		if con is not None:
			con.close()
		ae_ent_id.delete(0,END)
		ae_ent_name.delete(0,END)
		ae_ent_salary.delete(0,END)
		ae_ent_id.focus()

def f11():
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["EMS_11Jan"]
		coll=db["employee"]
		Id=(ue_ent_id.get())
		if (Id == '' ):
			raise Exception("ID cannot be blank!")
		elif(not Id.lstrip("-").isdigit() and Id!=""):
			raise Exception("ID should have only numbers!")
		else:
			Id=int(Id)
			if(Id<0):
				raise Exception("Id cannot be less than zero!")
		name=ue_name_ent.get()
		if(name==""):
			raise Exception("name cannot be empty!")
		elif(not name.isalpha() and name!=""):
			raise Exception("name should contain only alphabets!")
		else:
			if(len(name)<3):
				raise Exception("Name should have minimum 3 alphabets!")
		salary=(ue_salary_ent.get())
		if(salary==""):
			raise Exception("salary cannot be empty!")
		elif(not salary.lstrip("-").isdigit() and salary!=""):
			raise Exception("salary must have only numbers!")
		else:
			salary = int(salary)
			if(salary<0):
				raise Exception("salary cannot be negative!")
			elif(salary<8000):
				raise Exception("salary should be more than 8000!")
			
		count=coll.count_documents({"_id":Id})
		if count==1:
				coll.update_one({"_id":Id},{"$set":{"name":name,"salary":salary}})
				showinfo("success","updated.")
		else:
			showerror(Id,"does not exists.")
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
		ue_ent_id.delete(0,END)
		ue_name_ent.delete(0,END)
		ue_salary_ent.delete(0,END)
		ue_ent_id.focus()
def f12():
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["EMS_11Jan"]
		coll=db["employee"]
		Id=de_ent_id.get()
		if (Id == '' ):
			raise Exception("ID cannot be blank!")
		elif(not Id.lstrip("-").isdigit() and Id!=""):
			raise Exception("ID should be only numbers!")
		else:
			Id=int(Id)
			if(Id<0):
				raise Exception("Id cannot be less than zero!")
		count=coll.count_documents({"_id":Id})
		if count==1:
			coll.delete_one({"_id":Id})
			showinfo("success","deleted successfully!")
		else:
			showerror(Id,"does not exists.")
	except Exception as e:
		showerror("issues",e)
	finally:
		if con is not None:
			con.close()
		de_ent_id.delete(0,END)
		de_lab_id.focus()

def f13():
	name=[]
	salary=[]
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["EMS_11Jan"]
		coll=db["employee"]
		data=coll.find().sort("salary",DESCENDING).limit(5)
		for d in data:
			name.append(d["name"])
			salary.append(d["salary"])
	except Exception as e:
			showerror("Issues",e)
	finally:
		if con is not None:
			con.close()
	plt.bar(name,salary,color="peachpuff",width=0.3)
	s=np.arange(len(name))
	plt.xticks(s,name)
	plt.xlabel("Names")
	plt.ylabel("Salary")
	plt.grid()
	plt.show()

def f14():
	ce.withdraw()
	root.deiconify()

def f17():
	answer=askyesno(title='confirmation',message='Are uh sure?')
	if answer:
		root.destroy()
root=Tk()
root.title("E.M.S")
root.geometry("500x600+50+50")
# root.config(bg="CadetBlue1")
root.config(bg="lightCyan2")

#adding buttons
f=("Arial",25,"bold")
btn_add=Button(root,text="Add",font=f,width=15,command=f1)
btn_add.pack(pady=10)
btn_view=Button(root,text="View",font=f,width=15,command=f2)
btn_view.pack(pady=10)
btn_update=Button(root,text="Update",font=f,width=15,command=f3)
btn_update.pack(pady=10)
btn_delete=Button(root,text="Delete",font=f,width=15,command=f4)
btn_delete.pack(pady=10)
btn_charts=Button(root,text="Chart",font=f,width=15,command=f5)
btn_charts.pack(pady=10)
lab_loc=Label(root,text="Location:",font=f)
lab_loc.place(x=25,y=450)
#code for location is here
wa="https://ipinfo.io/"
res=requests.get(wa)
data=res.json()
city=data["city"]
lab_locans=Label(root,text=city,font=f)
lab_locans.place(x=25,y=500)
#code for weather is here
a1="https://api.openweathermap.org/data/2.5/weather?"
a2="q="+city
a3="&appid="+"b3b45d946e5e7f73ccdfc6508b6af84b"
a4="&units="+"metric"
wa=a1+a2+a3+a4
res=requests.get(wa)
data=res.json()
# degree=chr(176)
msg=data["main"]["temp"]
mainmsg=str(msg)+'\u00B0'+"C"
lab_temp=Label(root,text="Temp:",font=f)
lab_tempAns=Label(root,text=mainmsg,font=f)
lab_tempAns.place(x=400,y=450)
lab_temp.place(x=280,y=450)



#view employee frontend
ve = Toplevel(root)
ve.title("View Student")
ve.geometry("500x600+50+50")
ve.config(bg="lightCyan2")
ve_st_data=ScrolledText(ve,width=22,height=10,font=f)
ve_btn_back=Button(ve,text="Back",font=f,command=f9)
ve_st_data.pack(pady=10)
ve_btn_back.pack(pady=10)
ve.withdraw()



#Update employee frontend
ue=Toplevel(root)
ue.title("Update Student")
ue.geometry("500x600+50+50")
ue.config(bg="lightCyan2")
#update ke id
ue_lab_id=Label(ue,text="Enter Id",font=f)
ue_lab_id.pack(pady=10)
#update id ka entry
ue_ent_id=Entry(ue,font=f,bd=2)
ue_ent_id.pack(pady=10)
#update name
ue_name_lab=Label(ue,text="Enter Name",font=f)
ue_name_lab.pack(pady=10)
ue_name_ent=Entry(ue,font=f,bd=2)
ue_name_ent.pack(pady=10)
#update salary
ue_salary_lab=Label(ue,text="Enter Salary:",font=f)
ue_salary_lab.pack(pady=10)
ue_salary_ent=Entry(ue,font=f,bd=2)
ue_salary_ent.pack(pady=10)
#update ke buttons
ue_save_btn=Button(ue,text="Save",font=f,command=f11)
ue_save_btn.pack(pady=10)
ue_back_btn=Button(ue,text="Back",font=f,command=f6)
ue_back_btn.pack(pady=10)
ue.withdraw()


#delete employee frontend
de=Toplevel(root)
de.title("Delete Employee")
de.geometry("500x600+50+50")
de.config(bg="lightCyan2")
de_lab_id=Label(de,text="Enter Id:",font=f)
de_lab_id.pack(pady=10)
de_ent_id=Entry(de,font=f,bd=2)
de_ent_id.pack(pady=10)
de_save_btn=Button(de,text="Save",font=f,command=f12)
de_save_btn.pack(pady=10)
de_back_btn=Button(de,text="Back",font=f,command=f7)
de_back_btn.pack(pady=10)
de.withdraw()

#add employee frontend
ae=Toplevel(root)
ae.title("Add Emp")
ae.geometry("500x600+50+50")
ae.config(bg="lightCyan2")
ae_lab_id=Label(ae,text="Enter Id:",font=f)
ae_lab_id.pack(pady=10)
ae_ent_id=Entry(ae,font=f,bd=2)
ae_ent_id.pack(pady=10)
ae_lab_name=Label(ae,text="Enter Name:",font=f)
ae_lab_name.pack(pady=10)
ae_ent_name=Entry(ae,font=f,bd=2)
ae_ent_name.pack(pady=10)
ae_lab_salary=Label(ae,text="Enter Salary:",font=f)
ae_lab_salary.pack(pady=10)
ae_ent_salary=Entry(ae,font=f,bd=2)
ae_ent_salary.pack(pady=10)
ae_save_btn=Button(ae,text="Save",font=f,command=f10)
ae_save_btn.pack(pady=10)
ae_back_btn=Button(ae,text="Back",font=f,command=f8)
ae_back_btn.pack(pady=10)
ae.withdraw()
ae.protocol("WM_DELETE_WINDOW",root.destroy)


ce=Toplevel(root)
ce.title("Charts")
ce.geometry("500x600+50+50")
ce.config(bg="lightCyan2")
ce_chart_btn=Button(ce,text="generate chart",font=f,command=f13)
ce_chart_btn.pack(pady=10)
ce_back_btn=Button(ce,text="back",font=f,command=f14)
ce_back_btn.pack(pady=10)
ce.withdraw()

root.protocol("WM_DELETE_WINDOW",f17)
root.mainloop()