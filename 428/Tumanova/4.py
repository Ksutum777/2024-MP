import math
import random
import numpy as np

         
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __mul_vect__(self, arg):
        return Vector(self.x * arg, self.y * arg, self.z * arg)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def spherical(self):
        r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        phi = math.atan2(self.y, self.x) 
        theta = math.atan2(self.z, math.sqrt(self.x**2 + self.y**2))
        return r, math.degrees(phi), math.degrees(theta)

           
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
    
class Radar(metaclass=Singleton):
    def get_relative_position(self, flying_object):
        relative_position = flying_object.position.__add__( (flying_object.velocity.__mul_vect__(flying_object.time)))
        relative_position.x -= self.position.x
        relative_position.y -= self.position.y
        relative_position.z -= self.position.z
        return relative_position
    def __init__(self,position):
        self.position=position
    
     


class Flying_object:
    def __init__(self, position, v):
        self.position = position
        self.velocity = v
        self.time = 0 

    def new_time(self, time):
        self.time = time
        
    
    def get_relative_pos_in_sk(self, radar):
        relative_position = radar.get_relative_position(self)
        return relative_position.spherical()
    def get_velocity(self):
        return self.velocity
    def __str__(self,value):
        return self.value
        
        
    
    

radar_place=Vector(0,0,0)
our_radar=Radar(radar_place)

print('Введите число летающих объектов')
number_flying_objects=int(input())

objects = []
for k in range(number_flying_objects):
        position = Vector(random.uniform(-10000, 10000),
                            random.uniform(-10000, 10000),
                            random.uniform(-10000, 10000))
        velocity = Vector(random.uniform(-800, 800),
                            random.uniform(-800, 800),
                            random.uniform(-800, 800))
        objects.append(Flying_object(position, velocity))
nums=[]
for i in range(len(objects)):
    nums.append(i+1)
print("Начальные координаты обьектов:\n")
for  i,obj in zip(nums,objects):
    r, theta, phi = obj.get_relative_pos_in_sk(our_radar)
    
    print(f"Object {i} \n  r={r},\t theta={theta},\t phi={phi}\n\n")
    
print("Введите время: ")
time = float(input())

print(f"Координаты обьектов спустя {time} секунд :\n")
for i,obj in zip (nums,objects):
    obj.new_time(time)
    r, theta, phi = obj.get_relative_pos_in_sk(our_radar)
    
    print(f"Object {i} \n r={r},\t theta={theta},\t phi={phi} \n\n")