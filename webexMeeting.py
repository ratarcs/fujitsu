#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests;

access_token = '********************'; 


listado = ["Listar usuarios", "Crear usuarios", "Mostrar detalles usuarios", "Actualizar un usuario", "Eliminar un usuario",
            "Listar Rooms", "Crear Rooms", "Detalles Rooms", "Detalles Room Meeting Info", "Actualizar Rooms", "Eliminar Rooms"]

print '\n'.join(map(str, listado))

opcionListado = raw_input('Escribe la opción deseada: ');


if opcionListado == listado[0]:
        apiUrl = "https://webexapis.com/v1/people";

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

        print(response.status_code)

        print(response.text)

elif opcionListado == listado[1]:
        emails = raw_input('Email de usuario: ');
        nombre = raw_input('Nombre del usuario: ');
        apellido = raw_input('Apellidos del usuario: ');

        apiUrl = "https://webexapis.com/v1/people";

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        body = { "emails": emails,
                "firstName": nombre,
                "lastName": apellidos}

        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.post(url=apiUrl, headers=httpHeaders, params=queryParams, json=body)

        print(response.status_code)

        print(response.text)
        
elif opcionListado == listado[2]:
        personId = raw_input('Id del usuario: ');

        apiUrl = "https://webexapis.com/v1/people/" + personId;

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

        print(response.status_code)

        print(response.text)

elif opcionListado == listado[3]:
        personId = raw_input('Id del usuario: ');

        apiUrl = "https://webexapis.com/v1/people/" + personId;

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.put(url=apiUrl, headers=httpHeaders, params=queryParams)

        print(response.status_code)

        print(response.text)

elif opcionListado == listado[4]:
        personId = raw_input('Id del usuario: ');

        apiUrl = "https://webexapis.com/v1/people/" + personId;

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.delete(url=apiUrl, headers=httpHeaders, params=queryParams)

        print(response.status_code)

        print(response.text)

elif opcionListado == listado[5]:

        apiUrl = "https://webexapis.com/v1/rooms/";

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

        print(response.status_code)

        print(response.text)

elif opcionListado == listado[6]:
        tituloRoom = raw_input('Título de Room: ');

        apiUrl = "https://webexapis.com/v1/rooms/";

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        body = { "title": tituloRoom}
        
        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.post(url=apiUrl, headers=httpHeaders, params=queryParams, json=body)

        print(response.status_code)

        print(response.text)

elif opcionListado == listado[7]:
        roomId = raw_input('Id de Room: ');

        apiUrl = "https://webexapis.com/v1/rooms/" + roomId;

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

        print(response.status_code)

        print(response.text)

elif opcionListado == listado[8]:
        roomId = raw_input('Id de Room: ');

        apiUrl = "https://webexapis.com/v1/rooms/" + roomId + "/meetingInfo";

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

        print(response.status_code)

        print(response.text)

elif opcionListado == listado[9]:
        roomId = raw_input('IdRoom de la sala: ');

        updateRoom = raw_input('Nuevo título de la sala: ');

        apiUrl = "https://webexapis.com/v1/rooms/" + roomId;

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        body = {"title": updateRoom}

        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.put(url=apiUrl, headers=httpHeaders, params=queryParams, json=body)

        print(response.status_code)

        print(response.text)

elif opcionListado == listado[10]:
        roomId = raw_input('IdRoom de la sala que deseas eliminar: ');

        apiUrl = "https://webexapis.com/v1/rooms/" + roomId;

        httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

        queryParams = {"sortBy" : "lastactivity", "max" : "2"}

        response = requests.delete(url=apiUrl, headers=httpHeaders, params=queryParams)

        print(response.status_code)

        print(response.text)

else:
         print("Incorrecto, escribe exactamente la opción.")
         