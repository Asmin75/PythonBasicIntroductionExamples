#program to convert km to miles
km = float(input("Enter the km:"))
conv_fac = 0.621371

miles = km * conv_fac
print("The %0.3f km is equal to %0.3f miles"%(km,miles))