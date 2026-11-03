# What is Inheritance?
# --Inheritance is a way of creating a ne class that inherits the properties of an existing class
# --The class gives properties is called parent class(Base Class)
# --The class that receives the properties is called child class(Derived Class)

# Purpose of Inheritance 
# -- Code reusability
# -- Reduce code duplication
# -- Improve code structure

# Real Life  example:
# Media is a parent class
# Audio, Video, Image are child classes

# Image attributes are like:
# -- width
# -- height
# -- color
# -- size

# Syntax of Inheritance

class Media:
    # Attributes of Media class
    pass

class Image(Media):
    # Attributes of Image class
    # Attributes of Media class
    pass

# Types of Inheritance:
# -- Single Inheritance
# -- Multiple Inheritance
# -- Multilevel Inheritance
# -- Hierarchical Inheritance
# -- Hybrid Inheritance

# -- SINGLE INHERITANCE
# When a child class inherits only one parent class, it is called Single Inheritance

# Example:
class Media:
    def setAttributes(self, width, height, color, size):
        self.width = width
        self.height = height
        self.color  = color
        self.size =  size 

    def getAttributes(self):
        print(self.width)
        print(self.height)
        print(self.color)
        print(self.size)

class Video(Media):
    def setVideoAttributes(self, duration):
        self.duration = duration

    def getVideoAttributes(self):
        print(self.duration)

video = Video()
video.setAttributes(500, 300, "blue", "260")
video.getAttributes()

video.setVideoAttributes(3000)
video.getVideoAttributes()

