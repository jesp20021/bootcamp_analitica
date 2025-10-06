persona={
    "nombre":"Mauricio",
    "edad":42,
    "ciudad":"Chiquinquira"
}
print(persona["edad"])
persona["nombre"]="juanito"
print(persona)
persona["edad"]="23"
print(persona)
persona["profesion"]="ingeniero"
print(persona)
print(persona.keys())# .keys me da todas las lleves y/o keys del diccionario
data2={
    "estrato":2,
    "eps":"sanitas",
    "comidas":["pastas","mexicana"],
    "profesion":"carnicero",
    "direccion":{
        "calle":"carrera",
        "numero":"75-26",
        "complemento":"apto 602"
    }
}
persona.update(data2)# para actualizar o modificar los valores de la lista o diccionario
print(persona)
print(f"nombre:{persona["nombre"]} apartamento: {persona["direccion"]}")
print(f"nombre:{persona["nombre"]} apartamento: {persona["direccion"]["complemento"]}")
print(f"segunda comida {persona["comidas"][1]}")