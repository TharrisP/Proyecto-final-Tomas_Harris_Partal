# Proyecto final de Tomas Harris Partal.

# Club deportivo

Este es un Proyecto Web Django con patrón MVT, en el cual se trabaja con distintas funcionalidades, incluyendo conceptos como herencia de HTML, admin, formularios, registros, permisos, CRUD y una base de datos.

**Cuenta con tres aplicaciones:**

   1. "app_busqueda": Esta aplicación comprende todo lo relacionado con los motores de búsqueda en la pagina web. Entre ellos se encuentra la busqueda de profesores, de actividades y de socios. Mas adelante se detallaran en profundidad.

   2. "app_user": La app permite loguearse, registrarse, todo lo que constituya la rama de perfiles y cuentas, tanto la edición, visión, como eliminación de dicha cuenta o perfil.

   3. "AppProyecto": Esta última es la que se encarga de la creación, edición, visualización y eliminación de los modelos creados; estos son---> SOCIOS - ACTIVIDADES - PROFESORES.

### SuperUser:
   - **Usuario:** Tomasharrispartal
   - **Contraseña:** tharrispar1216

## Descripción de secciones en el Sitio Web

1. **Inicio**
   - Lleva a la pagina principal. Es la única vista a la que tiene acceso el usuario sin iniciar sesión.

2. **Socios**
   - Al oprimir, aparece la lista actual de socios registrados en el club deportivo. Esta vista está *restringida* no solo para cuando no haya iniciado sesion el usuario, sino que además todos los usuarios que se registren e inicien sesión solo tienen acceso a la lista como se muestra en la tabla y a la información detallada de cada socio; es decir, no pueden modificar ni eliminar dicha información.

3. **Profesores**
   - Muestra la lista existente de los profesores registrados, se muestra en forma de tabla, y solamente como vista previa nombre y apellido. Al igual que el inciso anterior (socios), se puede desplegar más información de los profesores (como email y profesión); pero no eliminar ni modificar ninguno de los registros de dichos profesores.

4. **Actividades**
   - Si se clickea en esta página, se puede ver una tabla en la que figuran las actividades actualmente registradas en el sitio del club deportivo. Se permite acceder solamente a la información de la actividad que queramos visualizar, mostrando nombre y valor de la actividad.

5. **Nuevo Socio**
   - Al seleccionar este botón, se redirige a un formulario para registrar un nuevo socio. Tienen acceso todos los usuarios que se registren e inicien sesión; a no ser que lo restrinja el Administrador.

6. **Nuevo Profesor**
   - Al oprimir, se redirige a un formulario para registar un nuevo profesor. Tienen acceso todos los usuarios que se registren e inicien sesión; a no ser que lo restrinja el Administrador.

7. **Nueva Actividad**
   - Ingresando en la página, se muestra un formulario para registrar una nueva actividad. No tiene acceso ningún usuario que no sea de Staff o Administrador.

8. **Busquedas**
   - Esta sección redirecciona a una pagina secundaria que esta ligada con la app_busqueda. Aparecen los accesos a las páginas:

                              -->Busqueda Socio: Se busca un socio por su numero de documento.
                              -->Busqueda Profesor: Se busca un profesor por su profesión.
                              -->Busqueda Actividad: Se busca una actividad por su nombre.
   
   Todas las busquedas devuelven la información completa del modelo que se consulta.

9. **Iniciar sesion**
   -Solicita dos campos, nombre de usuario y contraseña. En caso de ingresar mal al menos uno de los campos, devuelve un mensaje de "Error en el ingreso de los datos"; y brinda la opción de intentar nuevamente iniciar sesión o registrarse.

10. **Crear cuenta**
   - Aparece un formulario de registro de usuario en el que solicitará usuario, email, contraseña y avatar (foto de perfil, es opcional).

#### Una vez iniciada la sesión:

11. **Ver perfil**
   - Figura nombre de usuario, email y, en caso de tener, la foto de perfil (sino aparece un mensaje de "No has subido un avatar"). En esta página se pueden observar dos botones:
                              *Editar Perfil*: Dirige a un formulario para modificar los datos de perfil.
                              *Eliminar Cuenta*: Aparece una pregunta de confirmación de eliminación de la cuenta.

12. **Cerrar sesión**
   - Se sale de la sesión actual, volviendo a la pagina principal y sin acceso a la mayoría de la informacion; solo se tiene acceso a la pagina principal y la busqueda de profesores, actividades.


**Navegacion:**
# Link de la pagina: 
    http://127.0.0.1:8000/

Principales Funcionalidades

Página principal           http://127.0.0.1:8000/
Lista de Socios            http://127.0.0.1:8000/lista-socios/
Lista de Profesores	      http://127.0.0.1:8000/lista-profesores/
Lista de actividades	      http://127.0.0.1:8000/lista-actividades/
Detalle Socio              http://127.0.0.1:8000/socio/detalle/1/
Detalle Profesor           http://127.0.0.1:8000/profesor/detalle/1/
Detalle Actividad          http://127.0.0.1:8000/actividad/detalle/1/
Nuevo Socio                http://127.0.0.1:8000/socio-form/
Nuevo Profesor             http://127.0.0.1:8000/profesor-form/
Nueva Actividad            http://127.0.0.1:8000/actividad/nuevo/
Busquedas                  http://127.0.0.1:8000/buscadores/
Ver Perfil                 http://127.0.0.1:8000/app_user/view-profile/
Cerrar Sesión              http://127.0.0.1:8000/app_user/logout/

