import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        if type(self.real_part)==str and type(self.imaginary_part)==str:
            raise ValueError('Invalid value for real and imaginary part')
        elif type(self.real_part)== str:
            raise ValueError('Invalid value for real part')
        elif type(self.imaginary_part)==str:
            raise ValueError('Invalid value for imaginary part')
                    
    def __str__(self):
        if self.imaginary_part <0:
            return '{}-{}i'.format(self.real_part,abs(self.imaginary_part))
        elif self.real_part <0 and self.imaginary_part >0:
            return '-{}+{}i'.format(abs(self.real_part),self.imaginary_part)
        else:
            return '{}+{}i'.format(self.real_part,self.imaginary_part)
            
    def conjugate(self):
            return ComplexNumber(self.real_part,-1*self.imaginary_part)
            
    def __add__(self,other):
        self.real_part+=other.real_part
        self.imaginary_part+=other.imaginary_part
        return ComplexNumber(self.real_part,self.imaginary_part)
            
    def __sub__(self,other):
        self.real_part-=other.real_part
        self.imaginary_part-=other.imaginary_part
        return ComplexNumber(self.real_part,self.imaginary_part)
    
    def __mul__(self,other):
        res_real=(self.real_part * other.real_part)-(self.imaginary_part * other.imaginary_part)
        res_imag=(self.imaginary_part * other.real_part)+(self.real_part * other.imaginary_part)
        return ComplexNumber(res_real,res_imag)
    
    def __truediv__(self,other):
        res_real=(self.real_part * other.real_part)+(self.imaginary_part * other.imaginary_part)
        res_imag=-1*(self.real_part* other.imaginary_part)+(self.imaginary_part * other.real_part)
        res_real/=(other.real_part**2+other.imaginary_part**2)
        res_imag/=(other.real_part**2+other.imaginary_part**2)
        return ComplexNumber(res_real,res_imag)
        
    def __abs__(self):
        absolute_value=math.sqrt(self.real_part**2+self.imaginary_part**2)
        return round((absolute_value),3)
    
    def __eq__(self,other):
        if self.real_part==other.real_part and self.imaginary_part ==other.imaginary_part:
            return True
        else:
            return False
