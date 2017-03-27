import random
f = open('pspmma.data','w')

#Variables declaration
backbones = 10
molecules = 30
atoms = backbones * molecules
xlo = 0
xhi = 50.0
ylo = 0
yhi = 50.0
zlo = 0
zhi = 10.0


f.write('LAMMPS Description\n')
f.write('\n')

f.write('%d atoms\n' %atoms)
f.write('%d bonds\n' %((backbones - 1) * molecules))
f.write('%d angles\n' %((backbones - 2) * molecules))
#f.write('%d dihedrals\n' %((backbones - 3) * molecules * 4)) 
f.write('\n')

f.write('2 atom types\n')
f.write('3 bond types\n')
f.write('4 angle types\n')
#f.write('5 dihedral types\n')
f.write('\n')

f.write('%d %.1f xlo xhi\n' %(xlo,xhi))
f.write('%d %.1f ylo yhi\n' %(ylo,yhi))
f.write('%d %.1f zlo zhi\n' %(zlo,zhi))
f.write('\n')

f.write('Masses\n')
f.write('\n')
f.write('1 100.0\n') #PS
f.write('2 104.0\n') #PMMA
f.write('\n')


f.write('Atoms\n')
f.write('\n')
t = 1
for y in range(molecules):
    for x in range(backbones):
	if y %2==0:
            if x < 5:
                f.write('%d %d 1 0 %d %d %d\n' %(t,y+1,x,y,0))
                t += 1
            else:
	        f.write('%d %d 2 0 %d %d %d\n' %(t,y+1,x,y,0))
	        t += 1
	else:
            if x < 5:
                f.write('%d %d 2 0 %d %d %d\n' %(t,y+1,x,y,0))
                t += 1
            else:
                f.write('%d %d 1 0 %d %d %d\n' %(t,y+1,x,y,0))
                t += 1
f.write('\n')

f.write('Bonds\n')
f.write('\n')
t = 1
for y in range(0,molecules):
	for z in range(1,backbones):
		if y %2==0:
			if z < 5:
				f.write('%d 1 %d %d\n' %(t,backbones * y + z,backbones * y + z + 1))
				t = t + 1
			elif z == 5:
				f.write('%d 3 %d %d\n' %(t,backbones * y + z,backbones * y + z + 1))
				t = t + 1
			elif z > 5:
				f.write('%d 2 %d %d\n' %(t,backbones * y + z,backbones * y + z + 1))
				t = t + 1
		else:
			if z < 5:
				f.write('%d 2 %d %d\n' %(t,backbones * y + z,backbones * y + z + 1))
				t = t + 1
			elif z == 5:
				f.write('%d 3 %d %d\n' %(t,backbones * y + z,backbones * y + z + 1))
				t = t + 1
			elif z > 5:
				f.write('%d 1 %d %d\n' %(t,backbones * y + z,backbones * y + z + 1))
				t = t + 1

f.write('\n')


f.write('Angles\n')
f.write('\n')
t = 1
for y in range(0,molecules):
	for z in range(1,backbones - 1):
		if y %2==0:
			if z <= 3:
				f.write('%d 1 %d %d %d\n' %(t,backbones * y + z,backbones * y + z + 1,backbones * y + z + 2))
				t = t+1
			elif z == 4:
				f.write('%d 3 %d %d %d\n' %(t,backbones * y + z,backbones * y + z + 1,backbones * y + z + 2))
				t = t+1	
			elif z == 5:
				f.write('%d 4 %d %d %d\n' %(t,backbones * y + z,backbones * y + z + 1,backbones * y + z + 2))
				t = t+1	
			elif z > 5:
				f.write('%d 2 %d %d %d\n' %(t,backbones * y + z,backbones * y + z + 1,backbones * y + z + 2))
				t = t+1
		else:
			if z <= 3:
				f.write('%d 2 %d %d %d\n' %(t,backbones * y + z,backbones * y + z + 1,backbones * y + z + 2))
				t = t+1
			elif z == 4:
				f.write('%d 4 %d %d %d\n' %(t,backbones * y + z,backbones * y + z + 1,backbones * y + z + 2))
				t = t+1	
			elif z == 5:
				f.write('%d 3 %d %d %d\n' %(t,backbones * y + z,backbones * y + z + 1,backbones * y + z + 2))
				t = t+1	
			elif z > 5:
				f.write('%d 1 %d %d %d\n' %(t,backbones * y + z,backbones * y + z + 1,backbones * y + z + 2))
				t = t+1
f.write('\n')

#f.write('Dihedrals\n')
#f.write('\n')
#t = 1
#for y in range(0,molecules):
#	for z in range(1,backbones - 2):
#		for a in range(1,5):
#			f.write('%d %d %d %d %d %d\n' %(t,a, backbones * y + z,backbones * y + z + 1,backbones * y + z + 2,backbones * y + z + 3))
#			t = t+1
#f.write('\n')
