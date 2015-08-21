var i = 1;
var tbody = document.getElementById('valueair');
var tbodyResult = document.getElementById('resultair');
var formvalue = document.getElementById('formvalue');
var counter = document.getElementById('counter');
var count=0;
var delRowButton=document.getElementById('delrowbutton');
delRowButton.disabled=true;
//отправка данных для расчета
$(document).ready(function() {
  

  $('#calculate').on('click', function() {
    $.ajax({
      url: '/loadingdiagram/calculate/',
      type: 'POST',
      dataType: "json",
      data: $('#formvalue').serialize(),
      success: function(response) {
        var i = 1
        console.log(response);
        while(i<=document.getElementById('resultair').getElementsByTagName('tr').length){
            var myResults = response;
            var rowResult = document.getElementById('resultair').getElementsByTagName('tr')[i-1];
            var j = 1;
            while(j<=4) {
                var td=rowResult.getElementsByTagName('td')[j];
                if (j==1){
                    td.innerHTML="";
                    var p =document.createElement('p');
                    p.align='center';
                    p.appendChild(document.createTextNode(myResults[i-1]['temperature_0'+i]));
                    td.appendChild(p);
                }else if (j==2){
                    td.innerHTML="";
                    var p =document.createElement('p');
                    p.align='center';
                    p.appendChild(document.createTextNode(myResults[i-1]['enthalpy_0'+i]));
                    td.appendChild(p);
                }else if (j==3){
                    td.innerHTML="";
                    var p =document.createElement('p');
                    p.align='center';
                    p.appendChild(document.createTextNode(myResults[i-1]['humiditycontent_0'+i]));                  
                    td.appendChild(p);
                }else if (j==4) {
                    td.innerHTML="";
                    var p =document.createElement('p');
                    p.align='center';
                    p.appendChild(document.createTextNode(myResults[i-1]['relativities_0'+i]));                   
                    td.appendChild(p);
                }
                    j++;
            }
            i++;
        }
              
      },
      error: function(errorThrown){
        alert('Что-то пошло не так');
        console.log(errorThrown);
      }
    });
    return false;
  });
}); 





//добавить поля для процессов
function addProcessesInput(){
    //Создаю select для выбора откуда делать мне расчет процесса
    var takeSelectRow=document.createElement('select');


    var valueSelect=this.options[this.selectedIndex].value;
    var tdProcesses=this.parentNode.nextSibling;
    var timeNowProcess=this.parentNode.nextSibling.nextSibling;
    var selectrow=this.parentNode.parentNode;
    var i=this.parentNode.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling.textContent;
    var inputElementTempr=this.parentNode.previousSibling.previousSibling.previousSibling.previousSibling.getElementsByTagName('input')[0];
    var inputElementEnthalpy=this.parentNode.previousSibling.previousSibling.previousSibling.getElementsByTagName('input')[0];
    var inputElementHumidit=this.parentNode.previousSibling.previousSibling.getElementsByTagName('input')[0];
    var inputElementRelat=this.parentNode.previousSibling.getElementsByTagName('input')[0];
    console.log(i);
    //
    if (valueSelect==1){
        inputElementTempr.readOnly=false;
        inputElementTempr.value="";
        inputElementEnthalpy.readOnly=false;
        inputElementEnthalpy.value="";
        inputElementHumidit.readOnly=false;
        inputElementHumidit.value="";
        inputElementRelat.readOnly=false;
        inputElementRelat.value="";  
        while (tdProcesses.getElementsByTagName('input').length){
            tdProcesses.getElementsByTagName('input')[0].remove();
        }
        while (timeNowProcess.getElementsByTagName('select').length){
            timeNowProcess.getElementsByTagName('select')[0].remove();
        }
        inputElementEnthalpy.readOnly=true;
        inputElementHumidit.readOnly=true;
        inputElementRelat.readOnly=true;
        var selectTimeNowProccess=document.createElement('select');
        selectTimeNowProccess.className='form-control';
        selectTimeNowProccess.id='selecttimenowproccess_0'+i;
        selectTimeNowProccess.name='selecttimenowproccess_0'+i;
        for (var k=0;k<i;k++) {
            if (k>0){
                var option=document.createElement('option')
                option.value = k;
                option.text  = 'Точка'+" "+k;
                selectTimeNowProccess.appendChild(option);
                timeNowProcess.appendChild(selectTimeNowProccess)
            }
        }
        
    } else if (valueSelect==0){
        inputElementTempr.readOnly=false;
        inputElementTempr.value="";
        inputElementEnthalpy.readOnly=false;
        inputElementEnthalpy.value="";
        inputElementHumidit.readOnly=false;
        inputElementHumidit.value="";
        inputElementRelat.readOnly=false;
        inputElementRelat.value="";   
        while (tdProcesses.getElementsByTagName('input').length){
            tdProcesses.getElementsByTagName('input')[0].remove();
        }
        while (timeNowProcess.getElementsByTagName('select').length){
            timeNowProcess.getElementsByTagName('select')[0].remove();
        }

    }else if (valueSelect==6){
        inputElementTempr.readOnly=false;
        inputElementTempr.value="";
        inputElementEnthalpy.readOnly=false;
        inputElementEnthalpy.value="";
        inputElementHumidit.readOnly=false;
        inputElementHumidit.value="";
        inputElementRelat.readOnly=false;
        inputElementRelat.value="";  
        while (tdProcesses.getElementsByTagName('input').length){
            tdProcesses.getElementsByTagName('input')[0].remove();
        }
        while (timeNowProcess.getElementsByTagName('select').length){
            timeNowProcess.getElementsByTagName('select')[0].remove();
        }
        var moisture=document.createElement('input');
        moisture.id='moisture_0'+i;
        moisture.name='moisture_0'+i;
        moisture.className='form-control';
        moisture.placeholder='Влагопоступение';
        var heatinput=document.createElement('input');
        heatinput.id='heatinput_0'+i;
        heatinput.name='heatinput_0'+i;
        heatinput.className='form-control';
        heatinput.placeholder='Теплопоступение';
        inputElementEnthalpy.readOnly=true;
        inputElementHumidit.readOnly=true;
        inputElementRelat.readOnly=true; 
        tdProcesses.appendChild(heatinput);
        tdProcesses.appendChild(document.createElement('p'));
        tdProcesses.appendChild(moisture);
        var selectTimeNowProccess=document.createElement('select');
        selectTimeNowProccess.className='form-control';
        selectTimeNowProccess.id='selecttimenowproccess_0'+i;
        selectTimeNowProccess.name='selecttimenowproccess_0'+i;
        for (var k=0;k<i;k++) {
            if (k>0){
                var option=document.createElement('option')
                option.value = k;
                option.text  = 'Точка'+" "+k;
                selectTimeNowProccess.appendChild(option);
                timeNowProcess.appendChild(selectTimeNowProccess)
            }
        } 

    }else if (valueSelect==7){
        inputElementTempr.readOnly=false;
        inputElementTempr.value="";
        inputElementEnthalpy.readOnly=false;
        inputElementEnthalpy.value="";
        inputElementHumidit.readOnly=false;
        inputElementHumidit.value="";
        inputElementRelat.readOnly=false;
        inputElementRelat.value="";  
        while (tdProcesses.getElementsByTagName('input').length){
            tdProcesses.getElementsByTagName('input')[0].remove();
        }
        while (timeNowProcess.getElementsByTagName('select').length){
            timeNowProcess.getElementsByTagName('select')[0].remove();
        }
        var moisture=document.createElement('input');
        moisture.id='moisture_0'+i;
        moisture.name='moisture_0'+i;
        moisture.className='form-control';
        moisture.placeholder='Влагопоступение';
        var heatinput=document.createElement('input');
        heatinput.id='heatinput_0'+i;
        heatinput.name='heatinput_0'+i;
        heatinput.className='form-control';
        heatinput.placeholder='Теплопоступение';
        inputElementEnthalpy.readOnly=true;
        inputElementTempr.readOnly=true;
        inputElementRelat.readOnly=true; 
        tdProcesses.appendChild(heatinput);
        tdProcesses.appendChild(document.createElement('p'));
        tdProcesses.appendChild(moisture);
        var selectTimeNowProccess=document.createElement('select');
        selectTimeNowProccess.className='form-control';
        selectTimeNowProccess.id='selecttimenowproccess_0'+i;
        selectTimeNowProccess.name='selecttimenowproccess_0'+i;
        for (var k=0;k<i;k++) {
            if (k>0){
                var option=document.createElement('option')
                option.value = k;
                option.text  = 'Точка'+" "+k;
                selectTimeNowProccess.appendChild(option);
                timeNowProcess.appendChild(selectTimeNowProccess)
            }
        } 

    }else if (valueSelect==8){
        inputElementTempr.readOnly=false;
        inputElementTempr.value="";
        inputElementEnthalpy.readOnly=false;
        inputElementEnthalpy.value="";
        inputElementHumidit.readOnly=false;
        inputElementHumidit.value="";
        inputElementRelat.readOnly=false;
        inputElementRelat.value="";  
        while (tdProcesses.getElementsByTagName('input').length){
            tdProcesses.getElementsByTagName('input')[0].remove();
        }
        while (timeNowProcess.getElementsByTagName('select').length){
            timeNowProcess.getElementsByTagName('select')[0].remove();
        }
        var moisture=document.createElement('input');
        moisture.id='moisture_0'+i;
        moisture.name='moisture_0'+i;
        moisture.className='form-control';
        moisture.placeholder='Влагопоступение';
        var heatinput=document.createElement('input');
        heatinput.id='heatinput_0'+i;
        heatinput.name='heatinput_0'+i;
        heatinput.className='form-control';
        heatinput.placeholder='Теплопоступение';
        inputElementHumidit.readOnly=true;
        inputElementTempr.readOnly=true;
        inputElementRelat.readOnly=true; 
        tdProcesses.appendChild(heatinput);
        tdProcesses.appendChild(document.createElement('p'));
        tdProcesses.appendChild(moisture);
        var selectTimeNowProccess=document.createElement('select');
        selectTimeNowProccess.className='form-control';
        selectTimeNowProccess.id='selecttimenowproccess_0'+i;
        selectTimeNowProccess.name='selecttimenowproccess_0'+i;
        for (var k=0;k<i;k++) {
            if (k>0){
                var option=document.createElement('option')
                option.value = k;
                option.text  = 'Точка'+" "+k;
                selectTimeNowProccess.appendChild(option);
                timeNowProcess.appendChild(selectTimeNowProccess)
            }
        } 

    }else if (valueSelect==9){
        inputElementTempr.readOnly=false;
        inputElementTempr.value="";
        inputElementEnthalpy.readOnly=false;
        inputElementEnthalpy.value="";
        inputElementHumidit.readOnly=false;
        inputElementHumidit.value="";
        inputElementRelat.readOnly=false;
        inputElementRelat.value="";  
        while (tdProcesses.getElementsByTagName('input').length){
            tdProcesses.getElementsByTagName('input')[0].remove();
        }
        while (timeNowProcess.getElementsByTagName('select').length){
            timeNowProcess.getElementsByTagName('select')[0].remove();
        }
        var capacity=document.createElement('input');
        capacity.id='capacity_0'+i;
        capacity.name='capacity_0'+i;
        capacity.className='form-control';
        capacity.placeholder='Мощность';
        var airMassFlow=document.createElement('input');
        airMassFlow.id='airmassflow_0'+i;
        airMassFlow.name='airmassflow_0'+i;
        airMassFlow.className='form-control';
        airMassFlow.placeholder='Масс.расход';
        inputElementHumidit.readOnly=true;
        inputElementEnthalpy.readOnly=true;
        inputElementTempr.readOnly=true;
        inputElementRelat.readOnly=true; 
        tdProcesses.appendChild(capacity);
        tdProcesses.appendChild(document.createElement('p'));
        tdProcesses.appendChild(airMassFlow);
        var selectTimeNowProccess=document.createElement('select');
        selectTimeNowProccess.className='form-control';
        selectTimeNowProccess.id='selecttimenowproccess_0'+i;
        selectTimeNowProccess.name='selecttimenowproccess_0'+i;
        for (var k=0;k<i;k++) {
            if (k>0){
                var option=document.createElement('option')
                option.value = k;
                option.text  = 'Точка'+" "+k;
                selectTimeNowProccess.appendChild(option);
                timeNowProcess.appendChild(selectTimeNowProccess)
            }
        } 

    }else if (valueSelect==4){
        inputElementTempr.readOnly=false;
        inputElementTempr.value="";
        inputElementEnthalpy.readOnly=false;
        inputElementEnthalpy.value="";
        inputElementHumidit.readOnly=false;
        inputElementHumidit.value="";
        inputElementRelat.readOnly=false;
        inputElementRelat.value="";  
        while (tdProcesses.getElementsByTagName('input').length){
            tdProcesses.getElementsByTagName('input')[0].remove();
        }
        while (timeNowProcess.getElementsByTagName('select').length){
            timeNowProcess.getElementsByTagName('select')[0].remove();
        }
        inputElementHumidit.readOnly=true;
        inputElementEnthalpy.readOnly=true;
        inputElementRelat.readOnly=true;
        var selectTimeNowProccess=document.createElement('select');
        selectTimeNowProccess.className='form-control';
        selectTimeNowProccess.id='selecttimenowproccess_0'+i;
        selectTimeNowProccess.name='selecttimenowproccess_0'+i;
        for (var k=0;k<i;k++) {
            if (k>0){
                var option=document.createElement('option')
                option.value = k;
                option.text  = 'Точка'+" "+k;
                selectTimeNowProccess.appendChild(option);
                timeNowProcess.appendChild(selectTimeNowProccess)
            }
        }

    }else if (valueSelect==10){
        inputElementTempr.readOnly=false;
        inputElementTempr.value="";
        inputElementEnthalpy.readOnly=false;
        inputElementEnthalpy.value="";
        inputElementHumidit.readOnly=false;
        inputElementHumidit.value="";
        inputElementRelat.readOnly=false;
        inputElementRelat.value="";  
        while (tdProcesses.getElementsByTagName('input').length){
            tdProcesses.getElementsByTagName('input')[0].remove();
        }
        while (timeNowProcess.getElementsByTagName('select').length){
            timeNowProcess.getElementsByTagName('select')[0].remove();
        }
        inputElementTempr.readOnly=true;
        inputElementEnthalpy.readOnly=true;
        inputElementRelat.readOnly=true;
        var selectTimeNowProccess=document.createElement('select');
        selectTimeNowProccess.className='form-control';
        selectTimeNowProccess.id='selecttimenowproccess_0'+i;
        selectTimeNowProccess.name='selecttimenowproccess_0'+i;
        for (var k=0;k<i;k++) {
            if (k>0){
                var option=document.createElement('option')
                option.value = k;
                option.text  = 'Точка'+" "+k;
                selectTimeNowProccess.appendChild(option);
                timeNowProcess.appendChild(selectTimeNowProccess)
            }
        }

    }else if (valueSelect==11){
        inputElementTempr.readOnly=false;
        inputElementTempr.value="";
        inputElementEnthalpy.readOnly=false;
        inputElementEnthalpy.value="";
        inputElementHumidit.readOnly=false;
        inputElementHumidit.value="";
        inputElementRelat.readOnly=false;
        inputElementRelat.value="";  
        while (tdProcesses.getElementsByTagName('input').length){
            tdProcesses.getElementsByTagName('input')[0].remove();
        }
        while (timeNowProcess.getElementsByTagName('select').length){
            timeNowProcess.getElementsByTagName('select')[0].remove();
        }
        inputElementHumidit.readOnly=true;
        inputElementEnthalpy.readOnly=true;
        inputElementTempr.readOnly=true;
        var selectTimeNowProccess=document.createElement('select');
        selectTimeNowProccess.className='form-control';
        selectTimeNowProccess.id='selecttimenowproccess_0'+i;
        selectTimeNowProccess.name='selecttimenowproccess_0'+i;
        for (var k=0;k<i;k++) {
            if (k>0){
                var option=document.createElement('option')
                option.value = k;
                option.text  = 'Точка'+" "+k;
                selectTimeNowProccess.appendChild(option);
                timeNowProcess.appendChild(selectTimeNowProccess)
            }
        }

    }
}


//добавляем строки
function addRow(){


    //creat row
    var row = document.createElement("TR");

    //add index td
    var td1 = document.createElement("TD");
    td1.appendChild(document.createTextNode(i));
    row.appendChild(td1);
  
    //add inputs td
    var fields = [
        {'name' : 'temperature_0',        'id' : 'temperature_0'},
        {'name' : 'enthalpy_0',           'id' : 'enthalpy_0'},
        {'name' : 'humiditycontent_0',    'id' : 'humiditycontent_0'},  
        {'name' : 'relativities_0',      'id' : 'relativities_0'}
    ]  
      
    for(var index in fields) {
        var inputElement       = document.createElement('input');
        inputElement.id        = fields[index]['id'] + i;
        inputElement.name      = fields[index]['name'] + i;
        inputElement.className = 'form-control';
        inputElement.type      = 'text';
        var td = document.createElement("td");
        td.appendChild(inputElement);
        row.appendChild(td);


    }
    //add result row
    var rowResult=document.createElement("TR");

    //add index tdresult
    var tdResult=document.createElement("td");
    tdResult.appendChild(document.createTextNode(i));
    tdResult.height='51';
    rowResult.appendChild(tdResult);
    //add parameters td
    var k=0;
    while (k<5){
        var td1Result = document.createElement("td");
        rowResult.appendChild(td1Result);
        k++;
    }

    //add select td
        var processes=[
        'По точ.',
        'Нагрев и охлаждение по температуре',
        'Охлаждение',
        'Увлажнение',
        'Ад.охлаждение по температуре',
        'Осушение',
        'Уг. коэф по температуре',
        'Уг. коэф по влагосодержанию',
        'Уг. коэф по энтальпии',
        'Нагрев по мощности',
        'Ад.охлаждение по влагосодержанию',
        'Ад.охлаждение по отн.влажности']; 

    var processes_select       = document.createElement("select");
    processes_select.className = 'form-control';
    processes_select.name      = 'processes_0'+i;
    processes_select.id        = 'processes_0'+i;
    




    for(var index in processes) {
        var option = document.createElement('option');
        option.value = index;
        option.text  = processes[index];
        processes_select.appendChild(option);
    }
  
    var processes_td = document.createElement("td");

    processes_td.appendChild(processes_select);
    row.appendChild(processes_td);
    //Селект для выбора начала процесса.
    var timeNowProcess=document.createElement("td");

    row.appendChild(timeNowProcess);


    tbodyResult.appendChild(rowResult);
            
    processes_select.setAttribute("onClick","addProcessesInput.call(this)");

    row.appendChild(document.createElement("td"));
    tbody.appendChild(row);
    i++;
    count++;
    //счетчик 
    counter.setAttribute('value',count);
    //активация удаление точки
    if (count>0){
        delRowButton.disabled=false;
    }

}





//удаляем строки
function delRow() {


    document.getElementById('valueair').deleteRow(-1);
    document.getElementById('resultair').deleteRow(-1);
    i--;
    count--;
    //счетчик 
    counter.setAttribute('value',count);
    //дисейбл buuton delRow
    if (count==0){
        delRowButton.disabled=true;
    }

}

