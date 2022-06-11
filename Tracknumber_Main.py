from tkinter import *
from mysqlx import OperationalError
import phonenumbers
from phonenumbers import geocoder,timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
#------------------------------------------------------------------------------
def search():
    
    entryNumber=entry.get()
    number=phonenumbers.parse(entryNumber)

    locate=geocoder.description_for_number(number,"en")
    countryvalue.config(text=locate)

    time=timezone.time_zones_for_number(number)
    zonevalue.config(text=time)

    geolocator=Nominatim(user_agent='geoapiExercises')
    location=geolocator.geocode(locate)

    lng=location.longitude
    lat=location.latitude
    longtitudevalue.config(text=lng)
    latitudevalue.config(text=lat)

    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M:%p")
    clockvalue.config(text=current_time)


root=Tk()
root.title("Phone Number Tracker")
root.iconbitmap("tkinter\\track phone number\\img\\phone_icon.ico")

# window and openscreen
w=365
h=584
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))
# root.resizable(width=0,height=0)

# logo and text
imgLogo=PhotoImage(file="tkinter\\track phone number\\img\\logoimage.png")
Label(root,image=imgLogo).place(x=240,y=70)
logoTxt=Label(root,text="Track Number",fg="#57adff",font=("arial",15,"bold")).place(x=85,y=113)



# entry for number 
entryPhoto=PhotoImage(file="tkinter\\track phone number\\img\\search png.png")
Label(root,image=entryPhoto).place(x=20,y=190)

entry=StringVar()
entryNumber=Entry(root,textvariable=entry,width=17,bd=0,font=("arial",20,"bold"),justify=("center"))
entryNumber.place(x=50,y=220)


# Button Search
searchPhoto=PhotoImage(file="tkinter\\track phone number\\img\\search.png")
searchButton=Button(image=searchPhoto,borderwidth=0,cursor="hand2",bd=0,font=("arial",16,"bold"),command=search)
searchButton.place(x=35,y=300)


# Button box

buttonPhoto=PhotoImage(file="tkinter\\track phone number\\img\\bottom png_copy.png")
Label(root,image=buttonPhoto).place(x=-2,y=355)

country=Label(root,text="country:",bg="#257e64",fg="black",font=("arial",11,"bold"))
country.place(x=38,y=400)
countryvalue=Label(root,text="",bg="#257e64",fg="white",font=("arial",10))
countryvalue.place(x=100,y=400)


zone=Label(root,text="TimeZone:",bg="#257e64",fg="black",font=("arial",11,"bold"))
zone.place(x=38,y=450)
zonevalue=Label(root,text="",bg="#257e64",fg="white",font=("arial",10))
zonevalue.place(x=115,y=450)


clock=Label(root,text="Phone Time:",bg="#257e64",fg="black",font=("arial",11,"bold"))
clock.place(x=200,y=400)
clockvalue=Label(root,text="",bg="#257e64",fg="white",font=("arial",10))
clockvalue.place(x=290,y=400)

longitude=Label(root,text="Longitude:",bg="#257e64",fg="black",font=("arial",11,"bold"))
longitude.place(x=38,y=500)
longtitudevalue=Label(root,text="",bg="#257e64",fg="white",font=("arial",11))
longtitudevalue.place(x=118,y=500)


latitude=Label(root,text="Latitude:",bg="#257e64",fg="black",font=("arial",11,"bold"))
latitude.place(x=200,y=500)
latitudevalue=Label(root,text="",bg="#257e64",fg="white",font=("arial",11))
latitudevalue.place(x=266,y=500)

root.mainloop()