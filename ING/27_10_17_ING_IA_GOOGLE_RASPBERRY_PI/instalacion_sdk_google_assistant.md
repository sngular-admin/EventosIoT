# {ing}tech_it : Instalación SDK Google Assistant API


Una vez hemos conectado por ssh a nuestra Raspberry Pi ya estamos en situación de poder instalar el SDK de Google Assistant para Python en nuestra Raspberry Pi.

Antes de instalar dicho SDK es aconsejable crear una cuenta gratuita de Google para desarrolladores en Google Cloud Platform con una cuenta de correo gmail la cual utilizaremos para todo los procesos de conectar la Raspberry Pi con nuestro bots y nuestra aplicación creada en Actions Google e integrada con nuestro bots. Para crear dicha cuenta podeis ir a este [enlace](https://cloud.google.com/?hl=es)

![GOOGLE CLOUD PLATFORM](./images/cloud_new_account.png)

Una vez que hemos creado la cuenta procedemos a instalar el SDK de Google Assistant para Python.

1. Autorizar a nuestra Raspberry Pi con nuestra cuenta de desarrollador.

1.1 Creamos un nuevo proyecto o seleccionamos uno ya existente [enlace](https://console.cloud.google.com/start)

![CREATE NEW PROJECT GOOGLE CLOUD PLATFORM](./images/create_project_google_cloud_platform.png)


1.2 Habilitamos las credenciales de la API

![ENABLE API CREDENTIALS](./images/enable_api_credential.png)

Una vez habilitada la API nos vamos a la pestaña credenciales en la pestaña "Credenciales" y creamos una credencial para nuestra Raspberry Pi que sea única para ella.

![CREATE CREDENTIAL FOR RASPBERRY PI](./images/create_credential_raspberry_pi.png)

1.3 Descargamos el fichero json con las credenciales y lo guardamos en la raiz de la raspberry pi, en el directorio "home/pi", lo podemos pasar por scp con este comando desde nuestro ordenador a la raspberry pi.

![DOWLOAD CREDENTIALS](./images/dowload_credential.png)

~~~
scp ~/Downloads/client_secret_client-id.json pi@raspberry-pi-ip-address:/home/pi/
~~~

[+AYUDA](https://developers.google.com/assistant/sdk/develop/python/config-dev-project-and-account)

1. Instalación del SDK de Google Assistant API para Python 3

Instalamos Python 3 y un entorno virtual (entorno virtual no es obligatorio)

~~~
sudo apt-get update
sudo apt-get install python3-dev python3-venv # Use python3.4-venv if the package cannot be found.
python3 -m venv env
env/bin/python -m pip install --upgrade pip setuptools
source env/bin/activate
~~~

Instalamos la librería del google assistant

~~~
python -m pip install --upgrade google-assistant-library
~~~

1. Probamos el ejemplo 
TODO

[+AYUDA](https://developers.google.com/assistant/sdk/develop/python/run-sample)
--------
Continuar al  [Paso 5](./creando_dialog_flow_y_action_google.md) o ir al [Indice](./index.md)