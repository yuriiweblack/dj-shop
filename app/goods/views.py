from django.shortcuts import render

# Create your views here.

def catalog(request):
    context = {
        'title': 'Home - Главная',
        'goods': [
            {
                "image": "deps/images/goods/table_and_three_chairs.jpg",
                "name": "Чайный столик и три стула",
                "description": "Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.",
                "price": 130.00,  
             },

             {
                "image": "deps/images/goods/table_and_two_chairs.jpg",
                "name": "Чайный столик и два стула",
                "description": "Набор из стола и двух стульев в минималистическом стиле.",
                "price": 95.00,  
             },

             {
                "image": "deps/images/goods/double_bed.jpg",
                "name": "Двухспальная кровать",
                "description": "Кровать двухспальная с надголовником и вообще очень ортопедичная.",
                "price": 700.00,  
             },

             {
                "image": "deps/images/goods/kitchen_table.jpg",
                "name": "Кухонный стол с раковиной",
                "description": "Кухонныйй стол для обеда с встроенной раковиной и стульями.",
                "price": 350.00,  
             },

             {
                "image": "deps/images/goods/kitchen_table2.jpg",
                "name": "Кухонный стол с встройкой",
                "description": "Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.",
                "price": 500.00,  
             },

             {
                "image": "deps/images/goods/corner_sofa.jpg",
                "name": "Угловой диван для гостинной",
                "description": "Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!",
                "price": 550.00,  
             },

             {
                "image": "deps/images/goods/bedside_table.jpg",
                "name": "Прикроватный столик",
                "description": "Прикроватный столик с двумявыдвижными ящиками (цветок не входит в комплект).",
                "price": 250.00,  
             },

             {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Диван обыкновенный",
                "description": "Диван, он же софа обыкновенная, ничего примечательного для описания.",
                "price": 180.00,  
             },

             {
                "image": "deps/images/goods/office_chair.jpg",
                "name": "Стул офисный",
                "description": "Описание товара, про то какой он классный, но это стул, что тут сказать...",
                "price": 70.00,  
             },

             {
                "image": "deps/images/goods/plants.jpg",
                "name": "Растение",
                "description": "Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.",
                "price": 20.00,  
             },

             {
                "image": "deps/images/goods/flower.jpg",
                "name": "Цветок стилизированный",
                "description": "Дизайнерский цветок (возможно искусственный) для украшения интерьера.",
                "price": 35.00,  
             },

             {
                "image": "deps/images/goods/strange_table.jpg",
                "name": "Прикроватный столик",
                "description": "Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.",
                "price": 33.00,  
             },

        ]
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    # context = {
    #     'title': 'Home - About',
    #     'content': 'About HOME',
    #     'some_text_about': 'About Lorem  ipsum dolor', 
    # }
    return render(request, 'goods/product.html')