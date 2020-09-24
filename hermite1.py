# Hermite spline interpolation

def f_spline(p0,p1,v0,v1,t):
	s1 = p0*(2*t**3-3*t**2+1)
	s2 = v1*(t**3-t**2)
	s3 = v0*(t**3-2*t**2+t)
	s4 = p1*(3*t**2-2*t**3)
	return s1+s2+s3+s4
 
def cv_controlpoints(interval,controlpoints,startx,endx):
	ax,ay = controlpoints[0][0],controlpoints[0][1]
	bx,by = controlpoints[1][0],controlpoints[1][1]
	cx,cy = controlpoints[2][0],controlpoints[2][1]
	dx,dy = controlpoints[3][0],controlpoints[3][1]
	list_to_return = []
	for t in range(startx,endx,interval):
		list_to_return.append([f_spline(ax,bx,cx,dx,t),f_spline(ay,by,cy,dy,t)])
	return list_to_return
  
print(cv_controlpoints(1,[[0,1],[2,3],[3,4],[5,6]],0,3))

