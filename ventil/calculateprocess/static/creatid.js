$(document).ready(function() {
  

  $('#creatid').on('click', function() {
    $.ajax({
      url: '/loadingdiagram/calculate/',
      type: 'POST',
      dataType: "json",
      data: $('#formvalue').serialize(),
      success: function(response) {
        
        var myResults = response;
















        var temperature=[-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,
        -24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,
        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
        25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41];
        var barometricpressure=document.getElementById('barometricpressure').value;
        
        function humid(temperature,barometricpressure,relativities){
            var saturationpressure
            var humiditycontentForId
            if (temperature<0){
                    saturationpressure=Math.exp((18.74 * temperature - 115.72) /(233.77 + 0.997 * temperature));
                }else{
                    saturationpressure=Math.exp(((16.57*temperature - 115.72)/(233.77+0.997*temperature)));
                } 
                    humiditycontentForId=(622*relativities/100*saturationpressure)/(barometricpressure-relativities/100*saturationpressure);
            return humiditycontentForId;
        }
        function temperature_for_enthalpy(enthalpy,humiditycontent){
            temperature=(enthalpy-2501*(humiditycontent/1000))/(1.006+1.805*(humiditycontent/1000));
            temperature.toFixed(2)
            return temperature;
        }
        function humid_for_enthalpy(enthalpy,temperature){
            humiditycontent=(enthalpy-1.006*temperature)*1000/(2501+1.805*temperature);
            humiditycontent.toFixed(2)
            return humiditycontent;
        }
        var placeholder = $("#flot-placeholder");



        var number=0;
        var HumidAndTemprValue=[];
     
        var value=[]
        var value2=[]
        var value3=[]
        var value4=[]
        var value5=[]
        var value6=[]
        var value7=[]
        var value8=[]
        var value9=[]
        var value10=[]
        while (number<80) {
                value.push([humid(temperature[number],barometricpressure,10),temperature[number]]);
                value2.push([humid(temperature[number],barometricpressure,20),temperature[number]]);
                value3.push([humid(temperature[number],barometricpressure,30),temperature[number]]);
                value4.push([humid(temperature[number],barometricpressure,40),temperature[number]]);
                value5.push([humid(temperature[number],barometricpressure,50),temperature[number]]);
                value6.push([humid(temperature[number],barometricpressure,60),temperature[number]]);
                value7.push([humid(temperature[number],barometricpressure,70),temperature[number]]);
                value8.push([humid(temperature[number],barometricpressure,80),temperature[number]]);
                value9.push([humid(temperature[number],barometricpressure,90),temperature[number]]);
                value10.push([humid(temperature[number],barometricpressure,100),temperature[number]]);
                number++;
                HumidAndTemprValue.push(value);
                HumidAndTemprValue.push(value2);
                HumidAndTemprValue.push(value3);
                HumidAndTemprValue.push(value4);
                HumidAndTemprValue.push(value5);
                HumidAndTemprValue.push(value6);
                HumidAndTemprValue.push(value7);
                HumidAndTemprValue.push(value8);
                HumidAndTemprValue.push(value9);
                HumidAndTemprValue.push(value10);
            };      
        var n=-1;
        var enthalpy=-20;
        t=-20;
        var enthalpyList=[];
        var calcualteplot=[];
        while (n<6){
            var humiditycontent=0;
            n++;
            enthalpy=enthalpy+2;
            if (n==5){
                n=0
                t=t+5

            }
            if (t>=20){
                t=15
            }
            if (enthalpy==126){
                break;
            }

            calcualteplot.push([[0,temperature_for_enthalpy(enthalpy,0)],[humid_for_enthalpy(enthalpy,t),t]]);

        }






        var relativities_10={
            legend:{show: true},
            data: value,
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var relativities_20={
            legend:{show: true},
            data: value2,
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var relativities_30={
            legend:{show: true},
            data: value3,
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var relativities_40={
            legend:{show: true},
            data: value4,
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var relativities_50={
            legend:{show: true},
            data: value5,
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var relativities_60={
            legend:{show: true},
            data: value6,
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var relativities_70={
            legend:{show: true},
            data: value7,
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var relativities_80={
            legend:{show: true},
            data: value8,
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var relativities_90={
            legend:{show: true},
            data: value9,
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var relativities_100={
            legend:{show: true},
            data: value10,
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy1={
            legend:{show: true},
            data: [[0.935,-20],[0,-17.936]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }    
        var enthalpyenthalpy2={
            legend:{show: true},
            data: [[1.7452,-20],[0,-15.763]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy3={
            legend:{show: true},
            data: [[2.5569,-20],[0,-13.793]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }      
        var enthalpyenthalpy4={
            legend:{show: true},
            data: [[3.3687,-20],[0,-11.823]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy5={
            legend:{show: true},
            data: [[4.1804,-20],[0,-9.8522]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy6={
            legend:{show: true},
            data: [[2.9217,-15],[0,-7.8818]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy7={
            legend:{show: true},
            data: [[3.7304,-15],[0,-5.9113]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy8={
            legend:{show: true},
            data: [[4.5392,-15],[0,-3.9409]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy9={
            legend:{show: true},
            data: [[5.348,-15],[0,-1.9704]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy10={
            legend:{show: true},
            data: [[6.1567,-15],[0,0]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy11={
            legend:{show: true},
            data: [[4.8954,-10],[0,1.9704]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy12={
            legend:{show: true},
            data: [[5.7012,-10],[0,3.9409]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy13={
            legend:{show: true},
            data: [[6.507,-10],[0,5.9113]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy14={
            legend:{show: true},
            data: [[7.3129,-10],[0,7.8818]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy15={
            legend:{show: true},
            data: [[8.1187,-10],[0,9.8522]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy16={
            legend:{show: true},
            data: [[6.8548,-5],[0,11.823]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy17={
            legend:{show: true},
            data: [[7.6577,-5],[0,13.793]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }  
        var enthalpyenthalpy18={
            legend:{show: true},
            data: [[8.4606,-5],[0,15.764]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy19={
            legend:{show: true},
            data: [[9.2635,-5],[0,17.734]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy20={
            legend:{show: true},
            data: [[10.066,-5],[0,19.704]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy21={
            legend:{show: true},
            data: [[8.8,0],[0,21.675]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy22={
            legend:{show: true},
            data: [[9.6,0],[0,23.635]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy23={
            legend:{show: true},
            data: [[10.4,0],[0,25.616]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy24={
            legend:{show: true},
            data: [[11.2,0],[0,27.586]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy25={
            legend:{show: true},
            data: [[12,0],[0,29.557]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy26={
            legend:{show: true},
            data: [[10.731,5],[0,31.527]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy27={
            legend:{show: true},
            data: [[11.528,5],[0,33.498]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy28={
            legend:{show: true},
            data: [[12.325,5],[0,35.468]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy29={
            legend:{show: true},
            data: [[13.123,5],[0,37.438]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy30={
            legend:{show: true},
            data: [[13.92,5],[0,39.409]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy31={
            legend:{show: true},
            data: [[12.649,10],[0,41.379]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy32={
            legend:{show: true},
            data: [[13.443,10],[0,43.45]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy33={
            legend:{show: true},
            data: [[14.237,10],[0,45.32]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy34={
            legend:{show: true},
            data: [[15.031,10],[0,47.291]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy35={
            legend:{show: true},
            data: [[15.826,10],[0,49.261]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy36={
            legend:{show: true},
            data: [[14.552,15],[0,51.232]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy37={
            legend:{show: true},
            data: [[15.344,15],[0,53.202]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy38={
            legend:{show: true},
            data: [[16.135,15],[0,55.172]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy39={
            legend:{show: true},
            data: [[16.927,15],[0,57.143]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy40={
            legend:{show: true},
            data: [[17.718,15],[0,59.113]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy41={
            legend:{show: true},
            data: [[16.442,20],[4.3431,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy42={
            legend:{show: true},
            data: [[17.231,20],[5.1152,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy43={
            legend:{show: true},
            data: [[18.02,20],[5.8873,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy44={
            legend:{show: true},
            data: [[18.808,20],[6.6594,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy45={
            legend:{show: true},
            data: [[19.597,20],[7.4315,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy46={
            legend:{show: true},
            data: [[20.385,20],[8.2036,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy47={
            legend:{show: true},
            data: [[21.174,20],[8.9757,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy48={
            legend:{show: true},
            data: [[21.963,20],[9.7478,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy49={
            legend:{show: true},
            data: [[22.751,20],[10.52,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy50={
            legend:{show: true},
            data: [[23.54,20],[11.292,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy51={
            legend:{show: true},
            data: [[22.248,25],[12.064,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        } 
        var enthalpyenthalpy52={
            legend:{show: true},
            data: [[23.034,25],[12.836,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy53={
            legend:{show: true},
            data: [[23.82,25],[13.608,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }
        var enthalpyenthalpy54={
            legend:{show: true},
            data: [[24.605,25],[14.38,50]],
            color: "black",
            points: { show: false },
            lines: { show: true },

        }    
        var data=[relativities_10,relativities_20,relativities_30,relativities_40,relativities_50,
        relativities_60,relativities_70,relativities_80,relativities_90,relativities_100,enthalpyenthalpy1,enthalpyenthalpy2,enthalpyenthalpy3,enthalpyenthalpy4,
        enthalpyenthalpy5,enthalpyenthalpy6,enthalpyenthalpy7,enthalpyenthalpy8,enthalpyenthalpy9,enthalpyenthalpy10,enthalpyenthalpy11,enthalpyenthalpy12,
        enthalpyenthalpy13,enthalpyenthalpy14,enthalpyenthalpy15,enthalpyenthalpy16,enthalpyenthalpy17,enthalpyenthalpy18,enthalpyenthalpy19,enthalpyenthalpy20,
        enthalpyenthalpy21,enthalpyenthalpy22,enthalpyenthalpy23,enthalpyenthalpy24,enthalpyenthalpy25,enthalpyenthalpy26,enthalpyenthalpy27,enthalpyenthalpy28,
        enthalpyenthalpy29,enthalpyenthalpy30,enthalpyenthalpy31,enthalpyenthalpy32,enthalpyenthalpy33,enthalpyenthalpy34,enthalpyenthalpy35,enthalpyenthalpy36,
        enthalpyenthalpy37,enthalpyenthalpy38,enthalpyenthalpy39,enthalpyenthalpy40,enthalpyenthalpy41,enthalpyenthalpy42,enthalpyenthalpy43,enthalpyenthalpy44,
        enthalpyenthalpy45,enthalpyenthalpy46,enthalpyenthalpy47,enthalpyenthalpy48,enthalpyenthalpy49,enthalpyenthalpy50,enthalpyenthalpy51,enthalpyenthalpy52,enthalpyenthalpy53,enthalpyenthalpy54];

        var key=1
        while(key<=document.getElementById('resultair').getElementsByTagName('tr').length){
            if (myResults[key-1]['selectionofaction_0'+key]==0){
                var dotsValue={
                    legend:{show: true},
                    data: [[myResults[key-1]['humiditycontent_0'+numberconnect],myResults[key-1]['temperature_0'+numberconnect]],[myResults[key-1]['humiditycontent_0'+key],myResults[key-1]['temperature_0'+key]]],
                    color: "black",
                    points: { show: true },
                    lines: { show: true },
                    
            } 

                data.push(dotsValue);
            }else if (myResults[key-1]['processes_0'+key]==1){
                var numberconnect=document.getElementById('selecttimenowproccess_0'+key).value
                var dotsValue={
                    legend:{show: true},
                    data: [[myResults[numberconnect-1]['humiditycontent_0'+numberconnect],myResults[numberconnect-1]['temperature_0'+numberconnect]],[myResults[key-1]['humiditycontent_0'+key],myResults[key-1]['temperature_0'+key]]],
                    color: "red",
                    points: { show: true },
                    lines: { show: true },
                
            } 

                data.push(dotsValue);

            }else if (myResults[key-1]['processes_0'+key]==3){
                var numberconnect=document.getElementById('selecttimenowproccess_0'+key).value
                var dotsValue={
                    legend:{show: true},
                    data: [[myResults[numberconnect-1]['humiditycontent_0'+numberconnect],myResults[numberconnect-1]['temperature_0'+numberconnect]],[myResults[key-1]['humiditycontent_0'+key],myResults[key-1]['temperature_0'+key]]],
                    color: "blue",
                    points: { show: true },
                    lines: { show: true },
                
            } 

                data.push(dotsValue);

            }else if (myResults[key-1]['processes_0'+key]==5){
                var numberconnect=document.getElementById('selecttimenowproccess_0'+key).value
                var dotsValue={
                    legend:{show: true},
                    data: [[myResults[numberconnect-1]['humiditycontent_0'+numberconnect],myResults[numberconnect-1]['temperature_0'+numberconnect]],[myResults[key-1]['humiditycontent_0'+key],myResults[key-1]['temperature_0'+key]]],
                    color: '#FF02DF',
                    points: { show: true },
                    lines: { show: true },
                
            } 

                data.push(dotsValue);

            }else if (myResults[key-1]['processes_0'+key]==6){
                var numberconnect=document.getElementById('selecttimenowproccess_0'+key).value
                var dotsValue={
                    legend:{show: true},
                    data: [[myResults[numberconnect-1]['humiditycontent_0'+numberconnect],myResults[numberconnect-1]['temperature_0'+numberconnect]],[myResults[key-1]['humiditycontent_0'+key],myResults[key-1]['temperature_0'+key]]],
                    color: '#FF02DF',
                    points: { show: true },
                    lines: { show: true },
                
            } 

                data.push(dotsValue);

            }else if (myResults[key-1]['processes_0'+key]==7){
                var numberconnect=document.getElementById('selecttimenowproccess_0'+key).value
                var dotsValue={
                    legend:{show: true},
                    data: [[myResults[numberconnect-1]['humiditycontent_0'+numberconnect],myResults[numberconnect-1]['temperature_0'+numberconnect]],[myResults[key-1]['humiditycontent_0'+key],myResults[key-1]['temperature_0'+key]]],
                    color: '#FF02DF',
                    points: { show: true },
                    lines: { show: true },
                
            } 

                data.push(dotsValue);

            }else if (myResults[key-1]['processes_0'+key]==8){
                var numberconnect=document.getElementById('selecttimenowproccess_0'+key).value
                var dotsValue={
                    legend:{show: true},
                    data: [[myResults[numberconnect-1]['humiditycontent_0'+numberconnect],myResults[numberconnect-1]['temperature_0'+numberconnect]],[myResults[key-1]['humiditycontent_0'+key],myResults[key-1]['temperature_0'+key]]],
                    color: "red",
                    points: { show: true },
                    lines: { show: true },
                
            } 

                data.push(dotsValue);

            }else if (myResults[key-1]['processes_0'+key]==9){
                var numberconnect=document.getElementById('selecttimenowproccess_0'+key).value
                var dotsValue={
                    legend:{show: true},
                    data: [[myResults[numberconnect-1]['humiditycontent_0'+numberconnect],myResults[numberconnect-1]['temperature_0'+numberconnect]],[myResults[key-1]['humiditycontent_0'+key],myResults[key-1]['temperature_0'+key]]],
                    color: 'blue',
                    points: { show: true },
                    lines: { show: true },
                
            } 

                data.push(dotsValue);

            }else if (myResults[key-1]['processes_0'+key]==10){
                var numberconnect=document.getElementById('selecttimenowproccess_0'+key).value
                var dotsValue={
                    legend:{show: true},
                    data: [[myResults[numberconnect-1]['humiditycontent_0'+numberconnect],myResults[numberconnect-1]['temperature_0'+numberconnect]],[myResults[key-1]['humiditycontent_0'+key],myResults[key-1]['temperature_0'+key]]],
                    color: 'blue',
                    points: { show: true },
                    lines: { show: true },
                
            } 

                data.push(dotsValue);

            }
            key++;
            
        }


        var options = {


            yaxis: { 
                max: 38,
                min: -30,
                ticks: 68
            },
            xaxis: { 
                max: 20,
                min: 0,
                ticks: 20
            },
            grid: {
                color: 'black',
                verticalLines: true,   
                horizontalLines: true,
                outlineWidth: 10,
                mouseActiveRadius: 5,
                tickColor: 'grey',
                clickable: true,
                hoverable: true
            },
            colors:'black'
        };


        var placeholder = $("#flot-placeholder");
        var plot=$.plot($("#flot-placeholder"), data ,options);

        var o = plot.pointOffset({ x: 0.6, y: -21.1});
        var positionValue10=plot.pointOffset({x:value[70][0], y:value[70][1]});
        var positionValue20=plot.pointOffset({x:value2[70][0], y:value2[70][1]});
        var positionValue30=plot.pointOffset({x:value3[70][0], y:value3[70][1]});
        var positionValue40=plot.pointOffset({x:value4[70][0], y:value4[70][1]});
        var positionValue50=plot.pointOffset({x:value5[70][0], y:value5[70][1]});
        var positionValue60=plot.pointOffset({x:value6[70][0], y:value6[70][1]});
        var positionValue70=plot.pointOffset({x:value7[65][0], y:value7[65][1]});
        var positionValue80=plot.pointOffset({x:value8[64][0], y:value8[64][1]});
        var positionValue90=plot.pointOffset({x:value9[63][0], y:value9[63][1]});
        var positionValue100=plot.pointOffset({x:value10[62][0], y:value10[62][1]});
        var positionEnthalpy18=plot.pointOffset({x:calcualteplot[0][1][0], y:calcualteplot[0][1][1]});
        var positionEnthalpy_10=plot.pointOffset({x:calcualteplot[4][1][0], y:calcualteplot[4][1][1]});
        var positionEnthalpy0=plot.pointOffset({x:calcualteplot[9][1][0], y:calcualteplot[9][1][1]});
        var positionEnthalpy10=plot.pointOffset({x:calcualteplot[14][1][0], y:calcualteplot[14][1][1]});
        var positionEnthalpy20=plot.pointOffset({x:calcualteplot[19][1][0], y:calcualteplot[19][1][1]});
        var positionEnthalpy30=plot.pointOffset({x:calcualteplot[24][1][0], y:calcualteplot[24][1][1]});
        var positionEnthalpy40=plot.pointOffset({x:calcualteplot[29][1][0], y:calcualteplot[29][1][1]});
        var positionEnthalpy50=plot.pointOffset({x:calcualteplot[34][1][0], y:calcualteplot[34][1][1]});
        var positionEnthalpy60=plot.pointOffset({x:calcualteplot[39][1][0], y:calcualteplot[39][1][1]});
        placeholder.append("<div style='position:absolute;left:" + (positionEnthalpy18.left-10) + "px;top:" + (positionEnthalpy18.top+20) + "px;color:#000000;transform:rotate(50deg);font-size:medium;'>-18 кДж/кг</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionEnthalpy_10.left-10) + "px;top:" + (positionEnthalpy_10.top+25) + "px;color:#000000;transform:rotate(50deg);font-size:medium'>-10 кДж/кг</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionEnthalpy0.left-10) + "px;top:" + (positionEnthalpy0.top+20) + "px;color:#000000;transform:rotate(50deg);font-size:medium'>0 кДж/кг</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionEnthalpy10.left-10) + "px;top:" + (positionEnthalpy10.top+20) + "px;color:#000000;transform:rotate(50deg);font-size:medium'>10 кДж/кг</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionEnthalpy20.left-10) + "px;top:" + (positionEnthalpy20.top+20) + "px;color:#000000;transform:rotate(50deg);font-size:medium'>20 кДж/кг</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionEnthalpy30.left-10) + "px;top:" + (positionEnthalpy30.top+20) + "px;color:#000000;transform:rotate(50deg);font-size:medium'>30 кДж/кг</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionEnthalpy40.left-10) + "px;top:" + (positionEnthalpy40.top+20) + "px;color:#000000;transform:rotate(50deg);font-size:medium'>40 кДж/кг</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionEnthalpy50.left-10) + "px;top:" + (positionEnthalpy50.top+20) + "px;color:#000000;transform:rotate(50deg);font-size:medium'>50 кДж/кг</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionEnthalpy60.left-10) + "px;top:" + (positionEnthalpy60.top+20) + "px;color:#000000;transform:rotate(50deg);font-size:medium'>60 кДж/кг</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionValue10.left-30) + "px;top:" + (positionValue10.top) + "px;color:#000000;transform:rotate(-75deg);background: white;font-size:x-small'>10 %</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionValue20.left-30) + "px;top:" + (positionValue20.top) + "px;color:#000000;transform:rotate(-68deg);background: white;font-size:x-small'>20 %</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionValue30.left-35) + "px;top:" + (positionValue30.top) + "px;color:#000000;transform:rotate(-60deg);background: white;font-size:x-small'>30 %</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionValue40.left-45) + "px;top:" + (positionValue40.top) + "px;color:#000000;transform:rotate(-50deg);background: white;font-size:x-small'>40 %</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionValue50.left-45) + "px;top:" + (positionValue50.top) + "px;color:#000000;transform:rotate(-40deg);background: white;font-size:x-small'>50 %</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionValue60.left-45) + "px;top:" + (positionValue60.top) + "px;color:#000000;transform:rotate(-35deg);background: white;font-size:x-small'>60 %</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionValue70.left-45) + "px;top:" + (positionValue70.top) + "px;color:#000000;transform:rotate(-30deg);background: white;font-size:x-small'>70 %</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionValue80.left-45) + "px;top:" + (positionValue80.top) + "px;color:#000000;transform:rotate(-30deg);background: white;font-size:x-small'>80 %</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionValue90.left-45) + "px;top:" + (positionValue90.top) + "px;color:#000000;transform:rotate(-30deg);background: white;font-size:x-small'>90 %</div>");
        placeholder.append("<div style='position:absolute;left:" + (positionValue100.left-45) + "px;top:" + (positionValue100.top-5) + "px;color:#000000;transform:rotate(-30deg);background: white;font-size:x-small'>100 %</div>");
 
    },
      error: function(errorThrown){
        alert('Что-то пошло не так');
        console.log(errorThrown);
      }
    });
    return false;
  });
});