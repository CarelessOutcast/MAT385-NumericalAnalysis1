#	Bezier plot procedure

import numpy as np
import matplotlib.pyplot as plt

def bezierplot(a,b,c,d):
	t=np.linspace(0.,1.,50,endpoint=True)
	bx=3*(b[0]-a[0]);    by=3*(b[1]-a[1])	# spline equations ...
	cx=3*(c[0]-b[0])-bx; cy=3*(c[1]-b[1])-by
	dx=d[0]-a[0]-bx-cx;  dy=d[1]-a[1]-by-cy
	xp=a[0]+t*(bx+t*(cx+t*dx))				
	yp=a[1]+t*(by+t*(cy+t*dy))
	return plt.plot(xp,yp)            # Plot spline curve
	


fig1=bezierplot([0,0], [.5,3], [0,7], [0,3])
fig2=bezierplot([0,0], [-.5,3], [0,7], [0,3])  #additional bezier curve

plt.show()
