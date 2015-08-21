# -*- coding: utf-8 -*- 
from math import *
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import RequestContext
from django.shortcuts import render_to_response
from calculation import ProcessCalculation
from django.http import JsonResponse
import json 

def calculate(request):
    i=1
    listvalue=[]
    counter=float(request.POST['counter'])
    while (i<=counter):
        processes=float(request.POST['processes_0'+str(i)])
        barometricpressure=request.POST['barometricpressure']
        temperature = request.POST['temperature_0'+str(i)]
        enthalpy = request.POST['enthalpy_0'+str(i)]
        humiditycontent = request.POST['humiditycontent_0'+str(i)]
        relativities = request.POST['relativities_0'+str(i)]
        parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
        #Реализация процессов
        if (parameters.enthalpy==u"" and parameters.humiditycontent==u"" and processes==0):
            parameters.find_valueair_with_temperature_and_relativities(parameters.temperature,parameters.relativities,barometricpressure)
        elif (parameters.humiditycontent==u"" and parameters.relativities==u"" and processes==0):
            parameters.find_valueair_with_temperature_and_enthalpy(parameters.temperature,parameters.enthalpy,barometricpressure)
        elif (parameters.enthalpy==u"" and parameters.relativities==u"" and processes==0):
            parameters.find_valueair_with_temperature_and_humiditycontent(parameters.temperature,parameters.humiditycontent,barometricpressure)
        elif (parameters.temperature==u"" and parameters.relativities==u"" and processes==0):
            parameters.find_valueair_with_humiditycontent_and_enthalpy(parameters.humiditycontent,parameters.enthalpy,barometricpressure)
        elif (parameters.temperature==u"" and parameters.enthalpy==u"" and processes==0):
            parameters.find_valueair_with_humiditycontent_and_relativities(parameters.humiditycontent,parameters.relativities,barometricpressure)
        elif (parameters.temperature==u"" and parameters.humiditycontent==u"" and processes==0):
            parameters.find_valueair_with_enthalpy_and_relativities(parameters.enthalpy,parameters.relativities,barometricpressure)
        elif (parameters.humiditycontent==u"" and parameters.enthalpy==u"" and parameters.relativities==u"" and processes==1):
            #Переменная j отвечает за элемент взятый из listvalue
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_hot(parameters.temperature,listvalue[j-1]['humiditycontent_0'+str(j)],barometricpressure)
        elif (parameters.humiditycontent==u"" and parameters.enthalpy==u"" and parameters.relativities==u"" and processes==6):
            #Переменная j отвечает за элемент взятый из listvalue
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            moisture=request.POST['moisture_0'+str(i)]
            heatinput=request.POST['heatinput_0'+str(i)]
            parameters.find_valueair_with_process_rayprocess_with_temperature(parameters.temperature,listvalue[j-1]['enthalpy_0'+str(j)],
            listvalue[j-1]['humiditycontent_0'+str(j)],moisture,heatinput,barometricpressure)
        elif (parameters.temperature==u"" and parameters.enthalpy==u"" and parameters.relativities==u"" and processes==7):
            #Переменная j отвечает за элемент взятый из listvalue
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            moisture=request.POST['moisture_0'+str(i)]
            heatinput=request.POST['heatinput_0'+str(i)]
            parameters.find_valueair_with_process_rayprocess_with_humiditycontent(parameters.humiditycontent,listvalue[j-1]['enthalpy_0'+str(j)],
            listvalue[j-1]['humiditycontent_0'+str(j)],moisture,heatinput,barometricpressure)
        elif (parameters.temperature==u"" and parameters.humiditycontent==u"" and parameters.relativities==u"" and processes==8):
            #Переменная j отвечает за элемент взятый из listvalue
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            moisture=request.POST['moisture_0'+str(i)]
            heatinput=request.POST['heatinput_0'+str(i)]
            parameters.find_valueair_with_process_rayprocess_with_enthalpy(enthalpy,listvalue[j-1]['enthalpy_0'+str(j)],
            listvalue[j-1]['humiditycontent_0'+str(j)],moisture,heatinput,barometricpressure)
        elif (parameters.temperature==u"" and parameters.humiditycontent==u"" and parameters.relativities==u"" and parameters.temperature==u"" and processes==9):
            #Переменная j отвечает за элемент взятый из listvalue
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            capacity=float(request.POST['capacity_0'+str(i)])
            airmassflow=float(request.POST['airmassflow_0'+str(i)])
            parameters.find_valueair_with_process_hot_with_capacit(capacity,airmassflow,listvalue[j-1]['enthalpy_0'+str(j)],
            listvalue[j-1]['humiditycontent_0'+str(j)],barometricpressure)
        #Адиабатное охлаждение
        elif (parameters.humiditycontent==u"" and parameters.relativities==u"" and parameters.enthalpy==u"" and processes==4):
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_adiabatic_cooling_with_temperature(temperature,listvalue[j-1]['enthalpy_0'+str(j)],barometricpressure)
        elif (parameters.temperature==u"" and parameters.relativities==u"" and parameters.enthalpy==u"" and processes==10):
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_adiabatic_cooling_with_humiditycontent(humiditycontent,listvalue[j-1]['enthalpy_0'+str(j)],barometricpressure)
        elif (parameters.humiditycontent==u"" and parameters.temperature==u"" and parameters.enthalpy==u"" and processes==11):
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_adiabatic_cooling_with_relativities(relativities,listvalue[j-1]['enthalpy_0'+str(j)],barometricpressure)

        some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
        }


        listvalue.append(some_data_to_dump)
        data = json.dumps(listvalue)
        i=i+1
    return HttpResponse(data, content_type='application/json') 
         
        


def process_calculation(request):
    return render(request, 'processcalculation.html')