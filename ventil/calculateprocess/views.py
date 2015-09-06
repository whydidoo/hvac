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
        selectionofaction=float(request.POST['selectionofaction_0'+str(i)])
        barometricpressure=request.POST['barometricpressure']
        if (selectionofaction==1):
            processes=float(request.POST['processes_0'+str(i)])
        elif(selectionofaction==0):
            dotvalue=float(request.POST['dotvalue_0'+str(i)])
        #Реализация процессов
        if (dotvalue==2):
            temperature = request.POST['temperature_0'+str(i)]
            enthalpy = 0
            humiditycontent = 0
            relativities = request.POST['relativities_0'+str(i)]
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_temperature_and_relativities(parameters.temperature,parameters.relativities,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'selectionofaction_0'+str(i):selectionofaction,
            }
        elif (dotvalue==0 and selectionofaction==0):
            temperature = request.POST['temperature_0'+str(i)]
            enthalpy = request.POST['enthalpy_0'+str(i)]
            humiditycontent = 0
            relativities = 0
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_temperature_and_enthalpy(parameters.temperature,parameters.enthalpy,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'selectionofaction_0'+str(i):selectionofaction,
            }
        elif (dotvalue==1 and selectionofaction==0):
            temperature = request.POST['temperature_0'+str(i)]
            enthalpy = 0
            humiditycontent = request.POST['humiditycontent_0'+str(i)]
            relativities = 0
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_temperature_and_humiditycontent(parameters.temperature,parameters.humiditycontent,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'selectionofaction_0'+str(i):selectionofaction,
            }
        elif (dotvalue==3 and selectionofaction==0):
            temperature = 0
            enthalpy = request.POST['enthalpy_0'+str(i)]
            humiditycontent = request.POST['humiditycontent_0'+str(i)]
            relativities = 0
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_humiditycontent_and_enthalpy(parameters.humiditycontent,parameters.enthalpy,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'selectionofaction_0'+str(i):selectionofaction,
            }
        elif (dotvalue==4 and selectionofaction==0):
            temperature = 0
            enthalpy = 0
            humiditycontent = request.POST['humiditycontent_0'+str(i)]
            relativities = request.POST['relativities_0'+str(i)]
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_humiditycontent_and_relativities(parameters.humiditycontent,parameters.relativities,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'selectionofaction_0'+str(i):selectionofaction,
            }
        elif (dotvalue==5 and selectionofaction==0):
            temperature = 0
            enthalpy = request.POST['enthalpy_0'+str(i)]
            humiditycontent = 0
            relativities = request.POST['relativities_0'+str(i)]
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_enthalpy_and_relativities(parameters.enthalpy,parameters.relativities,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'selectionofaction_0'+str(i):selectionofaction,
            }
        elif (processes==0 and selectionofaction==1):
            #Переменная j отвечает за элемент взятый из listvalue
            temperature=request.POST['lasttemperature_0'+str(i)]
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_hot(temperature,listvalue[j-1]['humiditycontent_0'+str(j)],barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'processes_0'+str(i):selectionofaction,
            }
        elif (processes==5 and selectionofaction==1):
            #Переменная j отвечает за элемент взятый из listvalue
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.temperature=request.POST['lasttemperature_0'+str(i)]
            moisture=request.POST['moisture_0'+str(i)]
            heatinput=request.POST['heatinput_0'+str(i)]
            parameters.find_valueair_with_process_rayprocess_with_temperature(parameters.temperature,listvalue[j-1]['enthalpy_0'+str(j)],
            listvalue[j-1]['humiditycontent_0'+str(j)],moisture,heatinput,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'processes_0'+str(i):processes,
            }
        elif (processes==6 and selectionofaction==1):
            #Переменная j отвечает за элемент взятый из listvalue
            parameters.humiditycontent=request.POST['lasthumiditycontent_0'+str(i)]
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            moisture=request.POST['moisture_0'+str(i)]
            heatinput=request.POST['heatinput_0'+str(i)]
            parameters.find_valueair_with_process_rayprocess_with_humiditycontent(parameters.humiditycontent,listvalue[j-1]['enthalpy_0'+str(j)],
            listvalue[j-1]['humiditycontent_0'+str(j)],moisture,heatinput,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'processes_0'+str(i):processes,
            }
        elif (processes==7 and selectionofaction==1):
            parameters.enthalpy=request.POST['lastenthalpy_0'+str(i)]
            #Переменная j отвечает за элемент взятый из listvalue
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            moisture=request.POST['moisture_0'+str(i)]
            heatinput=request.POST['heatinput_0'+str(i)]
            parameters.find_valueair_with_process_rayprocess_with_enthalpy(parameters.enthalpy,listvalue[j-1]['enthalpy_0'+str(j)],
            listvalue[j-1]['humiditycontent_0'+str(j)],moisture,heatinput,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'processes_0'+str(i):processes,
            }
        elif (processes==8 and selectionofaction==1):
            #Переменная j отвечает за элемент взятый из listvalue
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            capacity=float(request.POST['capacity_0'+str(i)])
            airmassflow=float(request.POST['airmassflow_0'+str(i)])
            parameters.find_valueair_with_process_hot_with_capacit(capacity,airmassflow,listvalue[j-1]['enthalpy_0'+str(j)],
            listvalue[j-1]['humiditycontent_0'+str(j)],barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'processes_0'+str(i):processes,
            }
        #Адиабатное охлаждение
        elif (processes==3 and selectionofaction==1):
            temperature=request.POST['lasttemperature_0'+str(i)]
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_adiabatic_cooling_with_temperature(temperature,listvalue[j-1]['enthalpy_0'+str(j)],barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'processes_0'+str(i):processes,
            }
        elif (processes==9 and selectionofaction==1):
            humiditycontent=request.POST['lasthumiditycontent_0'+str(i)]
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_adiabatic_cooling_with_humiditycontent(humiditycontent,listvalue[j-1]['enthalpy_0'+str(j)],barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'processes_0'+str(i):processes,
            }
        elif (processes==10 and selectionofaction==1):
            relativities=request.POST['lastrelativities_0'+str(i)]
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_adiabatic_cooling_with_relativities(relativities,listvalue[j-1]['enthalpy_0'+str(j)],barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): parameters.temperature,
            'enthalpy_0'+str(i): parameters.enthalpy,
            'humiditycontent_0'+str(i): parameters.humiditycontent,
            'relativities_0'+str(i): parameters.relativities,
            'processes_0'+str(i):processes,
            }

        listvalue.append(some_data_to_dump)
        data = json.dumps(listvalue)
        i=i+1
    return HttpResponse(data, content_type='application/json') 
         
        


def process_calculation(request):
    return render(request, 'processcalculation.html')