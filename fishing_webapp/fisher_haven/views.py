from django.shortcuts import render, redirect
from .models import SaleItem

def index(request):
    return render(request, 'index.html')

def catalogue(request):
    # Вывод товаров
    items = SaleItem.objects.all()  # Получаем все товары из базы данных
    context = {
        'items': items  # Передаем товары в контекст для отображения
    }
    return render(request, 'catalogue.html', context)

def add_item(request):
    # Добавление товара
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        image_url = request.POST.get('image_url')

        # Создаем новый товар и сохраняем его в базе данных
        new_item = SaleItem(
            name=name,
            price=price,
            quantity=quantity,
            description=description,
            image_url=image_url
        )
        new_item.save()
    return redirect('catalogue')  # Перенаправляем на страницу каталога после добавления товара

def delete_item(request, item_id):
    # Удаление товара
    item = SaleItem.objects.get(id=item_id)
    item.delete()
    return redirect('catalogue')