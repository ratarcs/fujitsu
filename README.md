# fujitsu

Guía de trabajo en Cisco Webex for Developer 

Existen varias manera de poder trabajar con Webex Meeting y por tanto, crear, modificar, eliminar o actualizar todas las API References que se necesite. 

POSTMAN

La primera parte sería desde POSTMAN haciendo las llamadas a la página https://webexapis.com. Dentro de la página https://developer.webex.com/docs/platform-introduction se puede encontrar en la sección API REFERENCES, todas las acciones de tipo GET, POST, DELETE y UPDATE para poder trabajar con postman. Para poder realizar todas las acciones correspondientes se debe utilizar credenciales de administrador  es decir, un BEARER TOKEN que encontramos una vez hecho el LOG IN en la parte derecha superior.


Una manera más fácil y accesible sería accediendo a las colecciones de POSTMAN donde el usuario/administrador puede obtener todas las llamadas a la API References. En el siguiente enlace se puede encontrar:  https://explore.postman.com/ciscodevnet. En particular se han utilizado: https://api.ciscospark.com y www.webexapis.com la cuál está asociada a las de prueba en Cisco Webex for Developer.



PYTHON

La otra forma de trabajo sería utilizando scripts con el lenguaje PYTHON en un IDE. En mi caso, se ha utilizado Visual Studio Code y se ha tenido que descargar la extensión Python for VSCode para poder trabajar más cómodamente. 

Dentro del repositorio https://github.com/ratarcs/fujitsu en GITHUB, se puede encontrar los scripts de PYTHON separados por el format .PY para poder utilizar según la instrucción que se necesite. A continuación se mostrará un ejemplo de cómo crear ROOMs en WEBEXAPIS :

pip install requests (Windows) // pip3 install requests (Mac)

import requests;

apiUrl = "https://webexapis.com/v1/rooms"; (Esta dirección puede cambiar según la acción a realizar)

access_token=”*****************************”; (Aqui se debe utilizar el bearer de admin)

httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

queryParams = {"sortBy" : "lastactivity", "max" : "2"}

response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)
(A continuación de requests irá seguido de GET, POST, PUT, DELETE para que en la apiUrl se pueda crear, modificar, eliminar ROOMs)


print(response.status_code) (Este código devuelve 200 si ha realizado una conexión y 403 si el access_token no es el correcto)

print(response.text) (Respuesta de la API con todos los datos nuevos)
