from django import forms


from .models import Producto

class formProduct(forms.ModelForm):

    class Meta:
        model = Producto
        fields = (
            'nombre_producto',
            'costo_presupuestado',
            'costo_real',
            'id_tienda',
            'comentarios',
            'unidad',
            'descripcion'
        )