"Demonstrating function evaluation at arbitrary points."

__author__ = "Anders Logg (logg@simula.no)"
__date__ = "2008-03-17 -- 2009-09-04"
__copyright__ = "Copyright (C) 2008 Anders Logg"
__license__  = "GNU LGPL Version 2.1"

# Modified by Johan Hake, 2009

from dolfin import *
from numpy import array

if not has_gts():
    print "DOLFIN must be compiled with GTS to run this demo."
    exit(0)

# Create mesh and a point in the mesh
mesh = UnitCube(8, 8, 8);
x = (0.31, 0.32, 0.33)

# A user-defined function
Vs = FunctionSpace(mesh, "CG", 2)
Vv = VectorFunctionSpace(mesh, "CG", 2)
fs = Function(Vs, "sin(3.0*x[0])*sin(3.0*x[1])*sin(3.0*x[2])")
fv = Function(Vv, ("sin(3.0*x[0])*sin(3.0*x[1])*sin(3.0*x[2])",
                   "1.0 + 3.0*x[0] + 4.0*x[1] + 0.5*x[2]","2"))

# Project to a discrete function
g = project(fs, Vs)

print """
Evaluate user-defined scalar function fs
fs(x) = %f
Evaluate discrete function g (projection of fs)
g(x) = %f
Evaluate user-defined vector valued function fv
fs(x) = %s"""%(fs(x),g(x),str(fv(x)))
