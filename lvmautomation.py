import subprocess
import time
print()
print()
print("Welcome to the program for LVM Automation")



#step2
ch='y'
pvdisks=''
while(ch=='y'or ch=='Y'):
	print('''Following is the list of devices available to be used as LVM:
		/sdf : 1G
		/sdg : 2G
		/sdh : 3G
		/sdi : 4G
		/sdc : 20G
		/sde : 30G
		/sdd : 40G''')
	x=input('Enter the disk you want to attach(1,2,3,4,2...) :')
	if x=='1':
		subprocess.getstatusoutput('pvcreate /dev/sdf')
		pvdisks=pvdisks+' '+'/dev/sdf'
	elif x=='2':
		subprocess.getstatusoutput('pvcreate /dev/sdg')
		pvdisks=pvdisks+' '+'/dev/sdg'
	elif x=='3':
		subprocess.getstatusoutput('pvcreate /dev/sdh')
		pvdisks=pvdisks+' '+'/dev/sdh'
	elif x=='4':
		subprocess.getstatusoutput('pvcreate /dev/sdi')
		pvdisks=pvdisks+' '+'/dev/sdi'
	elif x=='20':
		subprocess.getstatusoutput('pvcreate /dev/sdc')
		pvdisks=pvdisks+' '+'/dev/sdc'
	elif x=='30':
		subprocess.getstatusoutput('pvcreate /dev/sde')
		pvdisks=pvdisks+' '+'/dev/sde'
	elif x=='40':
		subprocess.getstatusoutput('pvcreate /dev/sdd')
		pvdisks=pvdisks+' '+'/dev/sdd'
	else:
		print('Please enter a valid data')
		exit()
	ch=input('Do you want to enter more devices?(y/n)')
#print(pvdisks)

print('')
vgname=input('Enter the name you want to give to you Volume Group: ')
cmdforvgcreate='vgcreate {}{}'.format(vgname,pvdisks)
#print('command for vg create:',cmdforvgcreate)
try:
	vgcreated=subprocess.getstatusoutput(cmdforvgcreate) 				#systemcommand
	if vgcreated[0]==0:
		print('Executing command...')
		time.sleep(1)
		print('Volume Group created successfully!')
	else:
		print('Unsuccessful')
		exit()
except:
	print('System error')
	exit()


print('')
lvname=input('Enter the name of logical volume you want to create: ')
lvsize=input('Enter the size of the logical volume(e.g 500M, 1G): ')
cmdforlvcreate='lvcreate --size {} --name {} {}'.format(lvsize,lvname,vgname)
#print('command for lv create:', cmdforlvcreate)
try:
	lvcreated=subprocess.getstatusoutput(cmdforlvcreate) 				#systemcommand
	if lvcreated[0]==0:
		print('Executing command...')
		time.sleep(1)
		print('Logical Volume created successfully!')
	else:
		print('Unsuccessful')
		exit()
except:
	print('System error')
	exit()



print('')
fstype=input('Enter the format type for your logical volume:')
cmdforformatting='mkfs.{} /dev/{}/{}'.format(fstype,vgname,lvname)
#print('Command for formatting:',cmdforformatting)
try:
	formatted=subprocess.getstatusoutput(cmdforformatting) 				#systemcommand
	if formatted[0]==0:
		print('Executing command...')
		time.sleep(1)
		print('Formatting successfully!')
	else:
		print('Unsuccessful')
		exit()
except:
	print('System error')
	exit()


print('')
dirname=input('Enter the name of directory for mounting your logical volume:')
cmdformkdir='mkdir /{}'.format(dirname)
try:
	dircreated=subprocess.getstatusoutput(cmdformkdir) 				#systemcommand
	if dircreated[0]==0:
		print('Executing command...')
		time.sleep(1)
		print('Directory created successfully!')
	else:
		print('Unsuccessful')
		exit()
except:
	print('System error')
	exit()



cmdformounting='mount /dev/{}/{} /{}'.format(vgname,lvname,dirname)
#print('Command for mounting: ',cmdformounting)
try:
	mounted=subprocess.getstatusoutput(cmdformounting) 				#systemcommand
	if mounted[0]==0:
		print('Executing command...')
		time.sleep(1)
		print('Formatting successfully!')
	else:
		print('Unsuccessful')
		exit()
except:
	print('System error')
	exit()


print('')
inc=input('Do you want to increase the size of logical volume?(y/n)')
if inc=='n':
	exit()
incrementsize=input('Enter the increment size (e.g 500M, 800M, 1G, 2G:): ')
cmdforlvextend='lvextend --size +{} /dev/{}/{}'.format(incrementsize,vgname,lvname)
print('Command for lvextend: ',cmdforlvextend)
try:
	lvextended=subprocess.getstatusoutput(cmdforlvextend) 				#systemcommand
	if lvextended[0]==0:
		print('Executing command...')
		time.sleep(1)
		print('Logical volume extended successfully!')
	else:
		print('Unsuccessful')
		exit()
except:
	print('System error')
	exit()

print('')
cmdforfsresizing='resize2fs /dev/{}/{}'.format(vgname,lvname)
#print('command for resizing file system:', cmdforfsresizing)
try:
	fsresized=subprocess.getstatusoutput(cmdforfsresizing) 				#systemcommand
	if fsresized[0]==0:
		print('Executing command...')
		time.sleep(1)
		print('File system resized successfully!')
	else:
		print('Unsuccessful')
		exit()
except:
	print('System error')
	exit()



print('')
choice=input('Do you want to add more storage device to your volume group?(y/n)')
if choice=='n':
	exit()
y=input('''Enter the disk you want to attach(1,2,3,4,2...)
		/sdf : 1G
		/sdg : 2G
		/sdh : 3G
		/sdi : 4G
		/sdc : 20G
		/sde : 30G
		/sdd : 40G: ''')
if y=='1':
	vgextenddevice='/dev/sdf'
elif y=='2':
	vgextenddevice='/dev/sdg'
elif y=='3':
	vgextenddevice='/dev/sdh'
elif y=='4':
	vgextenddevice='/dev/sdi'
elif y=='20':
	vgextenddevice='/dev/sdc'
elif y=='30':
	vgextenddevice='/dev/sde'
elif y=='40':
	vgextenddevice='/dev/sdd'
else:
	print('Please enter a valid data')
	exit()
cmdforvgextend='vgextend {} {}'.format(vgname,vgextenddevice)
try:
	vgextened=subprocess.getstatusoutput(cmdforvgextend) 				#systemcommand
	if vgextened[0]==0:
		print('Executing command...')
		time.sleep(1)
		print('Volume group extended successfully!')
	else:
		print('Unsuccessful')
		exit()
except:
	print('System error')
	exit()


print('')
inc=input('Do you want to add more space to your logical volume now?(y/n)')
if choice=='n':
	exit()
lvextendsize=input('''Enter size of logical volume you want to increase (e.g 500M, 800M, 1G, 2G): ''')
cmdforlvextend='lvextend --size +{} /dev/{}/{}'.format(lvextendsize,vgname,lvname)
#print('Command for lvextend: ',cmdforlvextend)
try:
	lvextenedagain=subprocess.getstatusoutput(cmdforlvextend) 				#systemcommand
	if lvextenedagain[0]==0:
		print('Executing command...')
		time.sleep(1)
		print('Logical volume extended successfully!')
	else:
		print('Unsuccessful')
		exit()
except:
	print('System error')
	exit()



print('')
cmdforfsresizing='resize2fs /dev/{}/{}'.format(vgname,lvname)
#print('command for resizing file system:', cmdforfsresizing)
try:
	fsresizedagain=subprocess.getstatusoutput(cmdforfsresizing) 				#systemcommand
	if fsresizedagain[0]==0:
		print('Executing command...')
		time.sleep(1)
		print('File system resized successfully!')
	else:
		print('Unsuccessful')
		exit()
except:
	print('System error')
	exit()
