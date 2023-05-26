import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "fFFtDutjsVWIBTD3j6q3ydyNY4ztEBtK"
print ("Bienvenido")
while True:
    orig = input("Destino de Inicio: ")
    if orig == "quit" or orig == "a":
        break
    dest = input("Destino Final: ")
    if dest == "quit" or dest == "a":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("Estado de la API: " + str(json_status) + " = Llamado completado.\n")
        print("=============================================")
        print("Direcciones " + orig + " hacia " + dest)
        print("Duracion del Viaje: " + json_data["route"]["formattedTime"])
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        
for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")

        print("=============================================")
json_status = json_data["info"]["statuscode"]

if json_status == 0:
        print("API Status: " + str(json_status) + " = Llamado exitoso a la ruta.\n")
json_status = json_data["info"]["statuscode"]

if json_status == 0:
        print("API Status: " + str(json_status) + " = Llamado exitoso a la ruta.\n")
if json_status == 0:
       
       for each in json_data["route"]["legs"][0]["maneuvers"]:
           print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
           print("=============================================\n")
elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
else:
        print("************************************************************************")
        print("Para Codigos de estado: " + str(json_status) + "; Refierase a:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

        