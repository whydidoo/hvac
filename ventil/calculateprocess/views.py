# -*- coding: utf-8 -*- 
from math import *
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import RequestContext
from django.shortcuts import render_to_response
from calculation import ProcessCalculation
from django.http import JsonResponse
import json 
import datetime
from django.utils import timezone

from . models import Feedback



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
        if (dotvalue==2 and selectionofaction==0):
            temperature = request.POST['temperature_0'+str(i)]
            enthalpy = 0
            humiditycontent = 0
            relativities = request.POST['relativities_0'+str(i)]
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_temperature_and_relativities(parameters.temperature,parameters.relativities,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'selectionofaction_0'+str(i):selectionofaction,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            }
        elif (dotvalue==0 and selectionofaction==0):
            temperature = request.POST['temperature_0'+str(i)]
            enthalpy = request.POST['enthalpy_0'+str(i)]
            humiditycontent = 0
            relativities = 0
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_temperature_and_enthalpy(parameters.temperature,parameters.enthalpy,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'selectionofaction_0'+str(i):selectionofaction,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            }
        elif (dotvalue==1 and selectionofaction==0):
            temperature = request.POST['temperature_0'+str(i)]
            enthalpy = 0
            humiditycontent = request.POST['humiditycontent_0'+str(i)]
            relativities = 0
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_temperature_and_humiditycontent(parameters.temperature,parameters.humiditycontent,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'selectionofaction_0'+str(i):selectionofaction,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            }
        elif (dotvalue==3 and selectionofaction==0):
            temperature = 0
            enthalpy = request.POST['enthalpy_0'+str(i)]
            humiditycontent = request.POST['humiditycontent_0'+str(i)]
            relativities = 0
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_humiditycontent_and_enthalpy(parameters.humiditycontent,parameters.enthalpy,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'selectionofaction_0'+str(i):selectionofaction,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            }
        elif (dotvalue==4 and selectionofaction==0):
            temperature = 0
            enthalpy = 0
            humiditycontent = request.POST['humiditycontent_0'+str(i)]
            relativities = request.POST['relativities_0'+str(i)]
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_humiditycontent_and_relativities(parameters.humiditycontent,parameters.relativities,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'selectionofaction_0'+str(i):selectionofaction,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            }
        elif (dotvalue==5 and selectionofaction==0):
            temperature = 0
            enthalpy = request.POST['enthalpy_0'+str(i)]
            humiditycontent = 0
            relativities = request.POST['relativities_0'+str(i)]
            parameters=ProcessCalculation(temperature,enthalpy,humiditycontent,relativities)
            parameters.find_valueair_with_enthalpy_and_relativities(parameters.enthalpy,parameters.relativities,barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'selectionofaction_0'+str(i):selectionofaction,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            }
        elif (processes==0 and selectionofaction==1):
            #Переменная j отвечает за элемент взятый из listvalue
            temperature=request.POST['lasttemperature_0'+str(i)]
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_hot(temperature,listvalue[j-1]['humiditycontent_0'+str(j)],barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):selectionofaction,
            'saturationtemperature_0'+str(i):parameters.saturationtemperature,
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
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
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            'airflowondew_0'+str(i):round(parameters.airflowondew),
            'airflowoncapacity_0'+str(i):round(parameters.airflowoncapacity),
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
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            'airflowondew_0'+str(i):round(parameters.airflowondew),
            'airflowoncapacity_0'+str(i):round(parameters.airflowoncapacity)
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
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            'airflowondew_0'+str(i):round(parameters.airflowondew),
            'airflowoncapacity_0'+str(i):round(parameters.airflowoncapacity)
            }
        elif (processes==8 and selectionofaction==1):
            #Переменная j отвечает за элемент взятый из listvalue
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            capacity=float(request.POST['capacity_0'+str(i)])
            airmassflow=float(request.POST['airmassflow_0'+str(i)])
            parameters.find_valueair_with_process_hot_with_capacit(capacity,airmassflow,listvalue[j-1]['enthalpy_0'+str(j)],
            listvalue[j-1]['humiditycontent_0'+str(j)],barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            }
        #Адиабатное охлаждение
        elif (processes==3 and selectionofaction==1):
            temperature=request.POST['lasttemperature_0'+str(i)]
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            airmassflow=request.POST['airmassflow_0'+str(i)]
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_adiabatic_cooling_with_temperature(temperature,listvalue[j-1]['enthalpy_0'+str(j)],barometricpressure,
            airmassflow,listvalue[j-1]['humiditycontent_0'+str(j)])
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            'airmoisture_0'+str(i):parameters.airmoisture,
            }
        elif (processes==9 and selectionofaction==1):
            airmassflow=request.POST['airmassflow_0'+str(i)]
            humiditycontent=request.POST['lasthumiditycontent_0'+str(i)]
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_adiabatic_cooling_with_humiditycontent(humiditycontent,listvalue[j-1]['enthalpy_0'+str(j)],
            barometricpressure,airmassflow,listvalue[j-1]['humiditycontent_0'+str(j)])
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            'airmoisture_0'+str(i):parameters.airmoisture,
            }
        elif (processes==10 and selectionofaction==1):
            airmassflow=request.POST['airmassflow_0'+str(i)]
            relativities=request.POST['lastrelativities_0'+str(i)]
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_adiabatic_cooling_with_relativities(relativities,listvalue[j-1]['enthalpy_0'+str(j)],
            barometricpressure,airmassflow,listvalue[j-1]['humiditycontent_0'+str(j)])
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            'airmoisture_0'+str(i):parameters.airmoisture,
            }
        elif (processes==2 and selectionofaction==1):
            airmassflow=request.POST['airmassflow_0'+str(i)]
            airmoisture=request.POST['airmoisture_0'+str(i)]
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_isothermicalmoisture_with_airmoisture(airmoisture,listvalue[j-1]['temperature_0'+str(j)],
            barometricpressure,airmassflow,listvalue[j-1]['humiditycontent_0'+str(j)],listvalue[j-1]['enthalpy_0'+str(j)])
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            'capacity_0'+str(i):parameters.capacity,
            }
        elif (processes==11 and selectionofaction==1):
            airmassflow=float(request.POST['airmassflow_0'+str(i)])
            relativities = float(request.POST['lastrelativities_0'+str(i)])
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_isothermicalmoisture_with_relativities(relativities,listvalue[j-1]['temperature_0'+str(j)],
            barometricpressure,airmassflow,listvalue[j-1]['enthalpy_0'+str(j)],listvalue[j-1]['humiditycontent_0'+str(j)])
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            'capacity_0'+str(i):parameters.capacity,
            'airmoisture_0'+str(i):parameters.airmoisture,
            }
        elif (processes==12 and selectionofaction==1):
            airmassflow=float(request.POST['airmassflow_0'+str(i)])
            humiditycontent= float(request.POST['lasthumiditycontent_0'+str(i)])
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            parameters.find_valueair_with_process_isothermicalmoisture_with_humiditycontent(humiditycontent,listvalue[j-1]['temperature_0'+str(j)],
            barometricpressure,airmassflow,listvalue[j-1]['enthalpy_0'+str(j)],listvalue[j-1]['humiditycontent_0'+str(j)])
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            'capacity_0'+str(i):parameters.capacity,
            'airmoisture_0'+str(i):parameters.airmoisture,
            }
        #Смешение 
        elif (processes==13 and selectionofaction==1):
            airmassflow=float(request.POST['airmassflow_0'+str(i)])
            airmassflowtwo=float(request.POST['airmassflowtwo_0'+str(i)])
            #Переменная j равна той строке в таблице с которой будет взаимодействовать процесс
            j=int(request.POST['selecttimenowproccess_0'+str(i)])
            dotval=int(request.POST['selecttimenowproccesstwo_0'+str(i)])
            parameters.find_valueair_with_process_mixing(airmassflow,airmassflowtwo,listvalue[j-1]['enthalpy_0'+str(j)],
            listvalue[dotval-1]['enthalpy_0'+str(dotval)],listvalue[j-1]['humiditycontent_0'+str(j)],
            listvalue[dotval-1]['humiditycontent_0'+str(dotval)],listvalue[j-1]['temperature_0'+str(j)],listvalue[dotval-1]['temperature_0'+str(dotval)],
            barometricpressure)
            some_data_to_dump = {
            'temperature_0'+str(i): round(parameters.temperature,2),
            'enthalpy_0'+str(i): round(parameters.enthalpy,2),
            'humiditycontent_0'+str(i): round(parameters.humiditycontent,2),
            'relativities_0'+str(i): round(parameters.relativities,2),
            'processes_0'+str(i):processes,
            'saturationtemperature_0'+str(i):round(parameters.saturationtemperature,2),
            'dewpoint_0'+str(i):round(parameters.dewpoint,2),
            'airdensity_0'+str(i):round(parameters.airdensity,2),
            'parcpressure_0'+str(i):round(parameters.parcpressure,2),
            'temperature_01'+str(i):parameters.temperature1,
            'temperature_02'+str(i):parameters.temperature2,
            'enthalpy_01'+str(i):parameters.enthalpy1,
            'enthalpy_02'+str(i):parameters.enthalpy2,
            'humiditycontent_01'+str(i):parameters.humiditycontent1,
            'humiditycontent_02'+str(i):parameters.humiditycontent2,
            'dotval_0'+str(i):dotval,
            }

        listvalue.append(some_data_to_dump)
        data = json.dumps(listvalue)
        i=i+1
    return HttpResponse(data, content_type='application/json') 
         
        


def process_calculation(request):
    return render(request, 'processcalculation.html')

def send_feedback(request):
    title  = request.POST['title_feedback']
    content = request.POST['content_feedback']
    date  = timezone.now()

    feedback = Feedback(title=title, content=content,date=date)
    feedback.save()
    return JsonResponse({'status': 'успешно', 'message' : 'WP'})