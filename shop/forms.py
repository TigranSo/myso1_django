from django import forms

from shop.models import OrderItem, Order


class AddQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']



class OrderUserView(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-input'
    class Meta:
         model = Order
         fields = ('location', 'home', 'podezd', 'etaj', 'kvartir', )