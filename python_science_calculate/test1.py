import scipy.optimize as opt
import numpy as np

def test_fmin_convolve(fminfunc, x, h, y, yn,x0):
	def convolve_func(h):
		return np.sum((yn - np.convolve(x, h))**2)
	h0 = fminfunc(convolve_func, x0)
	print fminfunc.__name__
	print "----------------"
	print 'error of y: ', np.sum((np.convolve(x, h0)-y)**2)/np.sum(y**2)
	print 'error of h: ', np.sum((h0-h)**2)/np.sum(h**2)
	print 

def test_n(m, n, nscale):
	x = np.random.rand(m)
	h = np.random.rand(n)
	y = np.convolve(x, h)
	yn = y + np.random.rand(len(y))*nscale
	x0 = np.random.rand(n)

	test_fmin_convolve(opt.fmin, x, h, y, yn, x0)
	test_fmin_convolve(opt.fmin_powell, x, h, y, yn, x0)
	test_fmin_convolve(opt.fmin_cg, x, h, y, yn, x0)
	test_fmin_convolve(opt.fmin_bfgs, x, h, y, yn, x0)

if __name__ =="__main__":
	test_n(200,20, 0.1)

