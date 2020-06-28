# fujitsu

Guía de trabajo en Cisco Webex for Developer 

Existen varias manera de poder trabajar con Webex Meeting y por tanto, crear, modificar, eliminar o actualizar todas las API References que se necesite. 

POSTMAN

La primera parte sería desde POSTMAN haciendo las llamadas a la página https://webexapis.com. Dentro de la página https://developer.webex.com/docs/platform-introduction se puede encontrar en la sección API REFERENCES, todas las acciones de tipo GET, POST, DELETE y UPDATE para poder trabajar con postman. Para poder realizar todas las acciones correspondientes se debe utilizar credenciales de administrador  es decir, un BEARER TOKEN que encontramos una vez hecho el LOG IN en la parte derecha superior.


Una manera más fácil y accesible sería accediendo a las colecciones de POSTMAN donde el usuario/administrador puede obtener todas las llamadas a la API References. En el siguiente enlace se puede encontrar:  https://explore.postman.com/ciscodevnet. En particular se han utilizado: https://api.ciscospark.com y www.webexapis.com la cuál está asociada a las de prueba en Cisco Webex for Developer.



PYTHON

La otra forma de trabajo sería utilizando scripts con el lenguaje PYTHON en un IDE. En mi caso, se ha utilizado Visual Studio Code y se ha tenido que descargar la extensión Python for VSCode para poder trabajar más cómodamente. 

Una vez descargado se debe instalar las dependencias de Requests.

$ pip install requests (Windows)

or

$ pip3 install requests (Mac)

Una vez terminado, se debe ejecutar mediante la instrucción:

python webexMeeting.py

Se debe escribir el mismo texto que aparece en el listado que aparece en terminal y seguir los pasos que demande la aplicación. Esta devolvera un JSON con todos los datos que deberiamos obtener de la misma manera que se haría, manualmente, en REFERENCES https://developer.webex.com/docs/platform-introduction.





