from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://web.whatsapp.com/")

from bs4 import BeautifulSoup
import requests
# from bs4 import BeautifulSoup
import requests
import PySimpleGUI as sg

# resposta = requests.get("https://web.whatsapp.com/")

resposta = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora</title>
    <script>

        let soma = null
        let numNov = null
        let apagarNum = false
        let ultSinal = null

        function clicou(num) {
            if (apagarNum == true){
                document.getElementById("numInt").value = null
                apagarNum = false
            }

            let val = document.getElementById("numInt")

            if (val.value == 0){
                document.getElementById("numInt").value = num

            }else{
                document.getElementById("numInt").value += num
            }
        }

        function operacoes(op){
            apagarNum = true
            let doc = parseInt(document.getElementById("numInt").value)

            if(soma == null){
            soma = doc

            }else if(numNov == null){

                numNov = doc

                if(op == 10){
                    document.getElementById("numInt").value = 0
                    soma = null
                    numNov = null
                }else if(op == 11){
                    soma += numNov
                }else if(op == 12){
                    soma -= numNov
                }else{
                    if (ultSinal == 11){
                        document.getElementById("numInt").value = soma + numNov
                        soma = doc
                    }else{
                        document.getElementById("numInt").value = soma - numNov
                        soma = doc
                    }


                    document.getElementById("numInt").value = soma
                }
                document.getElementById("numInt").value = soma
                numNov = null
            }
            console.log(soma)
            console.log(numNov)
            console.log(ultSinal)

            ultSinal = op
        }

    </script>



    <style>


        .btn{
            width: fit-content;
            border: 2px solid black;
            margin-top: 50px;
            margin-left: 650px;
            background-color: grey;
            border-radius: 10px;
            padding: 20px;
        }


        .visor{
            margin: 5px;
            height: 50px;
            border: 5px solid black;
        }


        input[type=button]{
            margin: 6px;
            border: none;
            background-color: #4CAF50; /* Green */
            color: white;
            padding: 17px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border: 2px solid black;
            border-radius: 10px;
            box-shadow: 0 3px 1px 0 black;
            text-align: center;
            padding: 15px;

        }


        input[type=button]:hover{
            transition-duration: 0.2s;
            background-color: white;
            color: black;
            border: 2px solid black;

        }


        input[type=button]:active{
            margin: 6px;
            border: none;
            background-color: seagreen	; /* Green */
            color: white;
            padding: 17px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border: 2px solid black;
            border-radius: 10px;
            box-shadow: 0 0px 0px 0 black;
            padding: 10px;
            transform: translateY(4px)


        }

        .CE{
            padding: 100px;

        }

        .numeros{
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            text-align: end;
            padding: 5px;
            font-size: 30px;
            width: 210px;
        }


    </style>
</head>
<body>





    <form class="btn">

        <div class="visor">
            <input type="text" class="numeros" id="numInt"></input>
        </div>
        
        <div class="visor2">
            <div class= "deus">
                <input type="text" class="numeros" id="numInt"></input>
            </div>
        </div>

        <input type="button" value="7" id="7" onclick=clicou(7)>
        <input type="button" value="8" id="8" onclick=clicou(8)>
        <input type="button" value="9" id="9" onclick=clicou(9)>
        <input class="CE" type="button" value="CE" onclick=operacoes(10)>
        <br>
        <input type="button" value="4" id="4" onclick=clicou(4)>
        <input type="button" value="5" id="5" onclick=clicou(5)>
        <input type="button" value="6" id="6" onclick=clicou(6)>
        <input type="button" value="+" onclick=operacoes(11)>
        <br>
        <input type="button" value="1" id="1" onclick=clicou(1)>
        <input type="button" value="2" id="2" onclick=clicou(2)>
        <input type="button" value="3" id="3" onclick=clicou(3)>
        <input type="button" value="-" onclick=operacoes(12)>
        <br>
        <input type="button" value="0" id="0" onclick=clicou(0)>
        <input type="button" value="=" id="=" onclick=operacoes(13)>



    </form>




</body>
</html>"""
print(resposta)

r = requests.get("https://web.whatsapp.com/")
bs = BeautifulSoup(str(r.text), 'html.parser')

print(bs.prettify())





bs = BeautifulSoup(str(resposta), 'html.parser')
# print(bs.prettify())


val = bs.find_all('div',{"class": "visor2"})


print(val)
for i in val:
    print(i.find_all({"class": "visor2"}))




html = BeautifulSoup(resposta.text, 'html.parser')
# valor = html.select('app')

