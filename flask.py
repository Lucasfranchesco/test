from flask import Flask
import random
facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
              "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
              "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
              "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
              "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo"]

moneda = random.randint(1,1)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1><a href = "/random">ver dato aleatorio</a> <a href = "/moneda">lanzador de moneda</a>'
    


@app.route("/random")
def factores():
    return f'<p>{random.choice(facts_list)}</p><a href = "/">volver al inicio</a>'

@app.route("/moneda")
def monedas():
    if moneda == 1:
        return f'<h1>cara, felicidades:)</h1> <a href = "/">volver al inicio</a>'
    if moneda == 2:
        return f'<h1>cruz, feicitaciones:)</h1> <a href = "/">volver al inicio</a>'
    

app.run(debug=True)
