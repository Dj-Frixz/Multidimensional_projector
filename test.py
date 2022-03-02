class Vect:
    '''
    A class to represent n-dimensional vectors.

    ...

    Attributes
    ----------
    coords : list or tuple
        the vector itself, written in its coordinates (x,y,z,w,...)
    dimensions : int
        number of dimensions of the vector
        if omitted, defaults to 3
        if greater than the length of coords, the empty spaces are automatically filled with 0

    Methods
    -------
    bruh():
        Prints 'bruh'.
    len():
        Returns the algebric length of the vector, so 'v.len()' stands for '||v||'
    sum -> a+b:
        Returns the sum of the elements of Vect a and Vect b in a Vect object
    product -> a*n:
        Returns the scalar multiplication of Vect a with a float n
    internal product -> a|b:
        Returns the internal/hermitian product of 2 vectors (Vect a|Vect b)
    '''

    def __init__(self,coords,dimensions=3) -> None:
        dim = len(coords)
        if dimensions<dim:
            raise AttributeError
        elif dimensions>dim:
            coords += [0]*(dimensions-dim)
        self.dim = dimensions
        self.elem = coords
        self.length = self.len()

    def __str__(self) -> str:
        string = '\n┎ ┒\n'
        for x in self.elem:
            string += '┃%s┃\n'%x
        string += '┖ ┚\n'
        return string
    
    def __repr__(self) -> str:
        return 'Vect object <'+repr(self.elem)+'>'

    '''
    def equalize(vect1,vect2):
        
        if vect1.dim==vect2.dim:
            return vect1,vect2,vect1.dim
        elif vect1.dim>vect2.dim:
            vect2.elem += [0]*(vect1.dim-vect2.dim)
            return vect1,vect2,vect1.dim
        else:
            vect1.elem += [0]*(vect2.dim-vect1.dim)
            return vect1,vect2,vect2.dim
    '''
    
    def __add__(self,v2) -> object:
        if self.dim==v2.dim:
            return Vect([self.elem[i]+v2.elem[i] for i in range(self.dim)],self.dim)
        elif self.dim>v2.dim:
            return Vect( [self.elem[i]+v2.elem[i] for i in range(v2.dim)] + self.elem[v2.dim:], self.dim)
        else:
            return Vect( [self.elem[i]+v2.elem[i] for i in range(self.dim)] + v2.elem[self.dim:], v2.dim)
    
    def __or__(self,v2) -> float:

        '''Returns the internal/hermitian product of 2 vectors'''

        res = 0
        n = self.dim if self.dim<v2.dim else v2.dim
        for i in range(n):
            res += self.elem[i]*v2.elem[i]
        return res
    
    def __mul__(self,n) -> object:
        return Vect([x*n for x in self.elem],self.dim)
    
    def len(self) -> float:
        from math import sqrt
        return sqrt(self.__or__(self))
    
    def rotate(self,angle,axis1=0,axis2=1,measure='rad') -> None:

        '''Rotates the vector changing only the axis1 and axis2 coordinates (for angle in degrees specify measure='deg')'''

        from math import sin,cos,radians,pi
        angle *= pi
        if measure=='deg': angle = radians(angle)
        s,c = sin(angle),cos(angle)
        k =                Vect((c,s) ,2)|self
        self.elem[axis2] = Vect((-s,c),2)|self
        self.elem[axis1] = k
    
    def bruh() -> None:
        print('bruh')

'''class Line():

    def __init__(self) -> None:
        pass
        
'''

class Cube:
    x = Vect((1,),1)
    y = Vect((0,1),2)
    z = Vect((0,0,1),3)


    def __init__(self,side,dimensions=3,pos=0) -> None:

        self.vectors = []
        for i in range(dimensions):
            self.vectors.append(Vect([0]*i,side),i+1)
        
        self.side = side
        self.dim = dimensions
    
    def chside(self,side) -> None:
        '''Changes the size of the cube by changing the side value.'''

        ratio = side/self.side
        for i in range(self.dim):
            self.vectors[i] *= ratio
        self.side = side
    
    def centre(self) -> Vect: 
        '''Returns the centre vector'''
        return (self.x+self.y+self.z)*0.5
    
    def rotate(self,angle,axis1=0,axis2=1):        
        '''Rotates the solid around one of its corners'''

        for i in range(self.dim):
            self.vectors[i].rotate(angle,axis1,axis2)
    
class Space:

    def __init__(self) -> None:
        pass

    def draw(self)
    
a = Vect([2,5,3])
b = Vect([2,3],2)
a.rotate(0.5)
print(a)