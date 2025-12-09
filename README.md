# Tarea-10-Odoo
1. Descripción del módulo
Este módulo permite gestionar los ordenadores de una empresa, sus componentes, el usuario que los utiliza y algunas incidencias. También calcula automáticamente el precio total del ordenador en función de los componentes que tiene.
El objetivo es practicar la creación de modelos, relaciones, restricciones, vistas y permisos en Odoo.

2. Estructura del módulo
El módulo está organizado así:

gestion_pc/
  __init__.py
  __manifest__.py
  models/
    component.py
    computer.py
    __init__.py
  views/
    component_view.xml
    computer_view.xml
    menu.xml
  security/
    ir.model.access.csv

3. Modelos creados
3.1. Modelo Component (pc.component)
Este modelo guarda la información de un componente usado en un ordenador.
Campos:

name: nombre del componente

specs: especificaciones

price: precio

currency_id: moneda usada

Se usa en una relación Many2many dentro del modelo del ordenador.

3.2. Modelo Computer (pc.computer)
Este modelo representa un ordenador.
Campos:
number: número o identificador del equipo
user_id: usuario asignado (Many2one a res.users)
components_ids: lista de componentes del ordenador (Many2many)
last_mod: última fecha de modificación
total_price: precio total calculado con los componentes
issues: incidencias
currency_id: moneda

4. Funciones principales del modelo
4.1. Restricción de fecha futura
@api.constrains('last_mod')
def _check_last_mod(self):
    for record in self:
        if record.last_mod and record.last_mod > date.today():
            raise ValidationError("La fecha no puede ser futura")


Esta función evita que se introduzcan fechas que aún no han ocurrido.

4.2. Cálculo del precio total
@api.depends("components_ids.price")
def _compute_total(self):
    for record in self:
        record.total_price = sum(record.components_ids.mapped("price"))


Cada vez que cambian los componentes del ordenador, este método suma sus precios y actualiza el precio total.

5. Seguridad
El archivo ir.model.access.csv define los permisos para que los usuarios internos de Odoo puedan crear, modificar, leer y borrar ordenadores y componentes.
Ejemplo de líneas del CSV:
access_pc_component,access_pc_component,model_pc_component,base.group_user,1,1,1,1
access_pc_computer,access_pc_computer,model_pc_computer,base.group_user,1,1,1,1

6. Vistas creadas
Vistas de componentes
Incluyen una vista lista y una vista formulario donde se pueden crear y editar componentes.
Vistas de ordenadores
Incluyen también lista y formulario. En el formulario se pueden añadir componentes y se muestra el precio total calculado.

7. Menú del módulo
El módulo añade un menú principal llamado "Gestión PC", que contiene dos submenús:
Componentes
Ordenadores
Cada uno abre su propia acción con las vistas correspondientes.

8. Instalación
Copiar la carpeta del módulo dentro de los addons.
Reiniciar Odoo.
Activar el modo desarrollador.

Actualizar la lista de aplicaciones.

Instalar el módulo.

9. Cómo usar el módulo
Para crear un componente: ir a Gestión PC → Componentes → Crear.
Para crear un ordenador: ir a Gestión PC → Ordenadores → Crear.
Al añadir componentes a un ordenador, el precio total se calcula automáticamente.
La fecha no puede ser futura.
