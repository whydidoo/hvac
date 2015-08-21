# -*- coding: utf-8 -*- 
from math import *
class ProcessCalculation:
    def __init__(self, temperature, enthalpy, humiditycontent, relativities):
        self.temperature = temperature
        self.enthalpy = enthalpy
        self.humiditycontent = humiditycontent
        self.relativities = relativities

#Нахождение параметоров с тепературой
    
    def find_valueair_with_temperature_and_enthalpy(self,temperature,enthalpy,barometricpressure):
        self.barometricpressure=float(barometricpressure) #Барометрическое давление
        self.temperature=float(temperature) #Температура
        self.enthalpy=float(enthalpy) #Энтальпия
        self.humiditycontent=round((self.enthalpy-1.006*self.temperature)*1000/
        (2501+1.805*self.temperature),5) #Влагосодержание
        self.parcpressure=round(self.barometricpressure*self.humiditycontent/
        (622+self.humiditycontent),5) #парциальное давление
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5)) 
        self.relativities=round(self.parcpressure/self.saturationpressure*100,5)#Отностилеьная влажность
        print(self.saturationpressure)

    def find_valueair_with_temperature_and_relativities(self,temperature,relativities,barometricpressure):
        self.barometricpressure=float(barometricpressure)
        self.temperature=float(temperature) 
        self.relativities=float(relativities)
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5)) 
        self.humiditycontent=round(622 * (self.relativities / 100 *self.saturationpressure) / 
        (self.barometricpressure - self.relativities / 100 * self.saturationpressure), 5)
        self.enthalpy=round(1.006 * self.temperature + self.humiditycontent / 
        1000 * (1.805 * self.temperature + 2501),5)#Энтальпия
        print(self.saturationpressure)

    def find_valueair_with_temperature_and_humiditycontent(self,temperature,humiditycontent,barometricpressure):
        self.barometricpressure=float(barometricpressure) #Барометрическое давление
        self.temperature=float(temperature) #Температура
        self.humiditycontent=float(humiditycontent)#Влагосодержание
        self.enthalpy=round(1.006 * self.temperature + self.humiditycontent / 
        1000 * (1.805 * self.temperature + 2501),5)#Энтальпия
        self.parcpressure=round(self.barometricpressure*self.humiditycontent/
        (622+self.humiditycontent),5) #парциальное давление
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5))   
        self.relativities=round(self.parcpressure/self.saturationpressure*100,5)#Отностилеьная влажность


    def find_valueair_with_humiditycontent_and_enthalpy(self,humiditycontent,enthalpy,barometricpressure):
        self.barometricpressure=float(barometricpressure) #Барометрическое давление
        self.humiditycontent=float(humiditycontent)#Влагосодержание
        self.enthalpy=float(enthalpy) #Энтальпия
        self.temperature=round((self.enthalpy-2501*(self.humiditycontent/1000))/
        (1.006+1.805*(self.humiditycontent/1000)), 5)#Температура
        self.parcpressure=round(self.barometricpressure*self.humiditycontent/
        (622+self.humiditycontent),5) #парциальное давление
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5)) 
        self.relativities=round(self.parcpressure/self.saturationpressure*100,5)#Отностилеьная влажность

    def find_valueair_with_humiditycontent_and_relativities(self,humiditycontent,relativities,barometricpressure):
        self.barometricpressure=float(barometricpressure)
        self.humiditycontent=float(humiditycontent)
        self.relativities=float(relativities)
        self.saturationpressure1=float((100*self.barometricpressure*self.humiditycontent/self.relativities)/
        (622+self.humiditycontent))
        self.temperature=-60
        self.saturationpressure=0
        while self.saturationpressure<self.saturationpressure1:
            self.temperature=self.temperature            
            if self.temperature<0:
                self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
                (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
            else:
                self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
                (233.77 + 0.997 * self.temperature)),5))
            self.temperature=round(self.temperature+0.001,5)
        self.enthalpy=round(1.006 * self.temperature + self.humiditycontent / 
        1000 * (1.805 * self.temperature + 2501),5)#Энтальпия

    def find_valueair_with_enthalpy_and_relativities(self,enthalpy,relativities,barometricpressure):
        self.barometricpressure=float(barometricpressure)
        self.enthalpy=float(enthalpy)
        self.relativities=float(relativities)
        self.saturationpressure=0
        self.humiditycontent=0
        self.humiditycontent_1=1
        self.temperature=-60
        while self.humiditycontent <= self.humiditycontent_1:
            self.temperature=self.temperature
            self.humiditycontent_1=float(round((self.enthalpy-1.006*self.temperature)*
            1000/(2501+1.805*self.temperature),5))
            if self.temperature<0:
                self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
                (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
            else:
                self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
                (233.77 + 0.997 * self.temperature)),5))
            self.humiditycontent=float(round(622 * (self.relativities / 
            100 * self.saturationpressure) / 
            (self.barometricpressure - self.relativities / 100 * self.saturationpressure),5))
            self.temperature=round(self.temperature+0.001,5)
        self.humiditycontent=round(622 * (self.relativities / 100 *self.saturationpressure) / 
        (self.barometricpressure - self.relativities / 100 * self.saturationpressure), 5)

    def find_valueair_with_process_hot(self,temperature,humiditycontent,barometricpressure):
        self.temperature=float(temperature)
        self.humiditycontent=float(humiditycontent)
        self.barometricpressure=float(barometricpressure)
        self.enthalpy=round(1.006 * self.temperature + self.humiditycontent / 
        1000 * (1.805 * self.temperature + 2501),5)#Энтальпия
        self.parcpressure=round(self.barometricpressure*self.humiditycontent/
        (622+self.humiditycontent),5) #парциальное давление
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5)) 
        self.relativities=round(self.parcpressure/self.saturationpressure*100,5)#Отностилеьная влажность

    def find_valueair_with_process_hot_with_capacit(self,capacity,airmassflow,previous_enthalpy,humiditycontent,barometricpressure):
        self.capacity=float(capacity)
        self.airmassflow=float(airmassflow)
        self.barometricpressure=float(barometricpressure)
        self.previous_enthalpy=float(previous_enthalpy)
        self.humiditycontent=float(humiditycontent)
        self.enthalpy=round(self.capacity/self.airmassflow+self.previous_enthalpy,5)
        self.temperature=round((self.enthalpy-2501*(self.humiditycontent/1000))/
        (1.006+1.805*(self.humiditycontent/1000)), 5)#Температура
        self.parcpressure=round(self.barometricpressure*self.humiditycontent/
        (622+self.humiditycontent),5) #парциальное давление
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5))  
        self.relativities=round(self.parcpressure/self.saturationpressure*100,5)#Отностилеьная влажность


    def find_valueair_with_process_rayprocess_with_temperature(self,temperature,previous_enthalpy,previous_humiditycontent,moisture,heatinput,barometricpressure):
        self.temperature=float(temperature)
        self.previous_enthalpy=float(previous_enthalpy)
        self.previous_humiditycontent=float(previous_humiditycontent)
        self.barometricpressure=float(barometricpressure)
        self.moisture=float(moisture)
        self.heatinput=float(heatinput)
        self.rayprocess=round(self.heatinput/self.moisture,5)
        self.humiditycontent=round((1.006 * self.temperature + self.rayprocess * 
        self.previous_humiditycontent - self.previous_enthalpy) / (self.rayprocess - (1.805 * self.temperature + 2501)/1000),5)#влага
        self.enthalpy=round(1.006 * self.temperature + self.humiditycontent / 
        1000 * (1.805 * self.temperature + 2501),5)#Энтальпия
        self.parcpressure=round(self.barometricpressure*self.humiditycontent/
        (622+self.humiditycontent),5) #парциальное давление
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5)) 
        self.relativities=round(self.parcpressure/self.saturationpressure*100,5)#Отностилеьная влажность

    def find_valueair_with_process_rayprocess_with_humiditycontent(self,humiditycontent,previous_enthalpy,previous_humiditycontent,moisture,
    heatinput,barometricpressure):
        self.humiditycontent=float(humiditycontent)
        self.previous_enthalpy=float(previous_enthalpy)
        self.previous_humiditycontent=float(previous_humiditycontent)
        self.barometricpressure=float(barometricpressure)
        self.moisture=float(moisture)
        self.heatinput=float(heatinput)
        self.rayprocess=round(self.heatinput/self.moisture,5)
        self.enthalpy=round(self.rayprocess*self.humiditycontent-self.rayprocess*self.previous_humiditycontent+self.previous_enthalpy,3)
        self.temperature=round((self.enthalpy-2501*(self.humiditycontent/1000))/
        (1.006+1.805*(self.humiditycontent/1000)), 5)#Температура
        self.parcpressure=round(self.barometricpressure*self.humiditycontent/
        (622+self.humiditycontent),5) #парциальное давление
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5))  
        self.relativities=round(self.parcpressure/self.saturationpressure*100,3)#Отностилеьная влажность

    def find_valueair_with_process_rayprocess_with_enthalpy(self,enthalpy,previous_enthalpy,previous_humiditycontent,moisture,
    heatinput,barometricpressure):
        self.enthalpy=float(enthalpy)
        self.previous_enthalpy=float(previous_enthalpy)
        self.previous_humiditycontent=float(previous_humiditycontent)
        self.barometricpressure=float(barometricpressure)
        self.moisture=float(moisture)
        self.heatinput=float(heatinput)
        self.rayprocess=round(self.heatinput/self.moisture,5)
        self.humiditycontent=round((self.previous_humiditycontent*self.rayprocess+self.enthalpy-self.previous_enthalpy)/self.rayprocess,3)        
        self.temperature=round((self.enthalpy-2501*(self.humiditycontent/1000))/
        (1.006+1.805*(self.humiditycontent/1000)), 5)#Температура
        self.parcpressure=round(self.barometricpressure*self.humiditycontent/
        (622+self.humiditycontent),5) #парциальное давление
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5)) 
        self.relativities=round(self.parcpressure/self.saturationpressure*100,5)#Отностилеьная влажность

    def find_valueair_with_process_adiabatic_cooling_with_temperature(self,temperature,previous_enthalpy,barometricpressure):
        self.barometricpressure=float(barometricpressure)
        self.temperature=float(temperature)
        self.enthalpy=float(previous_enthalpy)
        self.humiditycontent=round((self.enthalpy-1.006*self.temperature)*1000/
        (2501+1.805*self.temperature),5) #Влагосодержание
        self.parcpressure=round(self.barometricpressure*self.humiditycontent/
        (622+self.humiditycontent),5) #парциальное давление
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5)) 
        self.relativities=round(self.parcpressure/self.saturationpressure*100,5)#Отностилеьная влажность
        print(self.temperature,self.enthalpy)

    def find_valueair_with_process_adiabatic_cooling_with_humiditycontent(self,humiditycontent,previous_enthalpy,barometricpressure):
        self.barometricpressure=float(barometricpressure)
        self.humiditycontent=float(humiditycontent)
        self.enthalpy=float(previous_enthalpy)
        self.temperature=round((self.enthalpy-2501*(self.humiditycontent/1000))/
        (1.006+1.805*(self.humiditycontent/1000)), 5)#Температура
        self.parcpressure=round(self.barometricpressure*self.humiditycontent/
        (622+self.humiditycontent),5) #парциальное давление
        if self.temperature<0:
            self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
            (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
        else:
            self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
            (233.77 + 0.997 * self.temperature)),5)) 
        self.relativities=round(self.parcpressure/self.saturationpressure*100,5)#Отностилеьная влажность

    def find_valueair_with_process_adiabatic_cooling_with_relativities(self,relativities,previous_enthalpy,barometricpressure):
        self.barometricpressure=float(barometricpressure)
        self.relativities=float(relativities)
        self.enthalpy=float(previous_enthalpy)
        self.saturationpressure=0
        self.humiditycontent=0
        self.humiditycontent_1=1
        self.temperature=-60
        while self.humiditycontent <= self.humiditycontent_1:
            self.temperature=self.temperature
            self.humiditycontent_1=float(round((self.enthalpy-1.006*self.temperature)*
            1000/(2501+1.805*self.temperature),5))
            if self.temperature<0:
                self.saturationpressure=round(exp((18.74 * self.temperature - 115.72) / 
                (233.77 + 0.997 * self.temperature)),5)#давление насыщения 
            else:
                self.saturationpressure=float(round(exp((16.57 * self.temperature - 115.72) /
                (233.77 + 0.997 * self.temperature)),5))
            self.humiditycontent=float(round(622 * (self.relativities / 
            100 * self.saturationpressure) / 
            (self.barometricpressure - self.relativities / 100 * self.saturationpressure),5))
            self.temperature=round(self.temperature+0.001,5)
        self.humiditycontent=round(622 * (self.relativities / 100 *self.saturationpressure) / 
        (self.barometricpressure - self.relativities / 100 * self.saturationpressure), 5)