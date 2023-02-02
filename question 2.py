class validate:
    def validate_triangle(self,x,y,z):
        if x+y>=z and y+z>=x and z+x>=y:
            return "valid Triangle"
        else:
            return "Invalid Triangle"
    def validate_rectangle(self,w,x,y,z):
        if (w==x and y==z) or (w==y and x==z) or (w==z and x==y):
            return "valid rectangle"
        else:
            return "Invalid rectangle"
val=validate()
print(val.validate_triangle(3,4,5))
print(val.validate_rectangle(2,4,2,4))