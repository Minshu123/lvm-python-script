#!/usr/bin/env python
# coding: utf-8

# In[14]:


def mainprint():
    print("\t\t*************************MAIN...PAGE***********************************")
    print("1. PHYSICAL VOLUME")
    print("2. VOLUME GROUP")
    print("3. LOGICAL VOLUME")
    print("4. RUN COMMAND")
    print("5. CLEAR SCREEN")
    print("6. TERMINATE")
def physicalvolume():
    print("\t\t*************************PHYSICAL...VOLUME***********************************")
    print("1. DISPLAY PHYSICAL VOLUME")
    print("2. CREATE PHYSICAL VOLUME")
    print("3. DELETE PHYSICAL VOLUME")
    print("4. RUN COMMAND")
    print("5. GO TO PREVIOUS PAGE")
    print("6. CLEAR SCREEN")
    print("7. TERMINATE")

def volumegroup():
    print("\t\t*************************VOLUME...GROUP***********************************")
    print("1. DISPLAY VOLUME GROUP")
    print("2. CREATE VOLUME GROUP")
    print("3. DELETE VOLUME GROUP")
    print("4. EXTEND VOLUME GROUP")
    print("5. RUN COMMAND")
    print("6. GO TO PREVIOUS PAGE")
    print("7. CLEAR SCREEN")
    print("8. TERMINATE")

def logicalvolume():
    print("\t\t*************************LOGICAL...VOLUME***********************************")
    print("1. DISPLAY LOGICAL VOLUME")
    print("2. CREATE LOGICAL VOLUME")
    print("3. EXTEND LOGICAL VOLUME")
    print("4. DELETE LOGICAL VOLUME")
    print("5. CREATE FILE")
    print("6. MOUNT FILE")
    print("7. RUN COMMAND")
    print("8. GO TO PREVIOUS PAGE")
    print("9. CLEAR SCREEN")
    print("10. TERMINATE")
    


# In[ ]:


import os ,subprocess,sys
flag=True
command_flag=False
while flag:
    if command_flag==False:
        print(subprocess.getoutput("clear"))
        mainprint()
    else:
        command_flag=False
    choice=int(input("Enter your option:- "))
    if choice==1:
        pv=True
        print(subprocess.getoutput("clear"))	
        physicalvolume()
        while pv:
            pvchoice=int(input("Enter your option for physical volume:-"))
            if pvchoice==1:
                print(subprocess.getoutput("pvdisplay"))
            elif pvchoice==2:
                pvdrive=input("Enter the drive:-")
                print(subprocess.getoutput("pvcreate "+pvdrive))
            elif pvchoice==3:
                pvdrive=input("Enter the name of pv drive name :-")
                print(subprocess.getoutput("pvremove "+pvdrive))
            elif pvchoice==4:
                command=input("Enter command:-")
                print(subprocess.getoutput(command))
            elif pvchoice==5:
                pv=False
            elif pvchoice==6:
                print(subprocess.getoutput("clear"))
                physicalvolume()
            elif pvchoice==7:
                print("Program Terminated....")
                sys.exit()
            else:
                print("INVALID INPUT.....")
                
    elif choice==2:
        vg=True
        print(subprocess.getoutput("clear")) 
        volumegroup()
        while vg:
            vgchoice=int(input("Enter your option for volume group:-"))
            if vgchoice==1:
                print(subprocess.getoutput("vgdisplay"))
            elif vgchoice==2:
                vgname=input("Enter the name of volume group:-")
                vgpv=input("Enter the physical volume:-")
                print(subprocess.getoutput("vgcreate "+vgname+" "+vgpv))
            elif vgchoice==3:
                vgname=input("Enter the name of volume group:-")
                print(subprocess.getoutput("vgchange -an "+vgname))
                print(subprocess.getoutput("vgremove "+vgname))
            elif vgchoice==4:
                vgname=input("Enter the name of volume group:-")
                vgpv=input("Enter the physical volume")
                print(subprocess.getoutput("vgextend "+vgname+" "+vgpv))
            elif vgchoice==5:
                command=input("Enter command:-")
                print(subprocess.getoutput(command))
            elif vgchoice==6:
                vg=False
            elif vgchoice==7:
                print(subprocess.getoutput("clear"))
                volumegroup()
            elif vgchoice==8:
                print("Program Terminated....")
                sys.exit()
            else:
                print("INVALID INPUT....")
    elif choice==3:
        lv=True
        print(subprocess.getoutput("clear"))
        logicalvolume()
        while lv:
            lvchoice=int(input("Enter your option for logical volume:-"))
            if lvchoice==1:
                vgname=input("Enter the name of volume group:-")
                lvname=input("Enter the name of logical volume:-")
                print(subprocess.getoutput("lvdisplay "+vgname+"/"+lvname))
            elif lvchoice==2:
                #this will create the logical volume which takes input as volume group ,logical volume name ,and size of the 
                #partition
                vgname=input("Enter the name of volume group:-")
                lvname=input("Enter the name of logical volume:-")
                lvsize=input("Enter the size of lv partition:-")
                print(subprocess.getoutput("lvcreate --size "+lvsize+" --name "+lvname+" "+vgname))
                print("Now we are formatting the lv created")
                print(subprocess.getoutput("mkfs.ext4 /dev/"+vgname+"/"+lvname))
            elif lvchoice==3:
                vgname=input("Enter the name of volume group:-")
                lvname=input("Enter the name of logical volume:-")
                lvsize=input("Enter the size of storage you want to add in lv ")
                drive="/dev/"+vgname+"/"+lvname
                print(subprocess.getoutput("lvextend --size +"+lvsize+""+drive))
                print(subprocess.getoutput("resize2fs "+drive))
            elif lvchoice==4:
                vgname=input("Enter the name of volume group:-")
                lvname=input("Enter the name of logical volume:-")
                drive="/dev/"+vgname+"/"+lvname
                print(subprocess.getoutput("lvchange -an "+drive))
                print(subprocess.getoutput("lvremove "+drive))
            elif lvchoice==5:
                filepath=input("Enter the path of file:-")
                print(subprocess.getoutput("mkdir "+filepath))
            elif lvchoice==6:
                vgname=input("Enter the name of volume group:-")
                lvname=input("Enter the name of logical volume:-")
                file=input("Enter the path of file:-")
                drive="/dev/"+vgname+"/"+lvname
                print(subprocess.getoutput("mount "+drive+" "+file))
            elif lvchoice==7:
                command=input("Enter command:-")
                print(subprocess.getoutput(command))
            elif lvchoice==8:
                lv=False
            elif lvchoice==9:
                print(subprocess.getoutput("clear"))
                logicalvolume()
            elif lvchoice==10:
                print("Program Terminated....")
                sys.exit()
            else:
                print("INVALID INPUT.....")
    elif choice==4:
        command=input("Enter command:-")
        print(subprocess.getoutput(command))
        command_flag=True
    elif choice==5:
        print(subprocess.getoutput("clear"))
    elif choice==6:
        print("Program Terminated....")
        sys.exit()
    else:
        print("INVALID INPUT.....")
                
                
            


# In[15]:



# In[17]:





# In[ ]:




