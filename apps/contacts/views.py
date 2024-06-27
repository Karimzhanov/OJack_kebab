from django.shortcuts import render
from apps.contacts.models import Contacts, Contact, Reservation
from apps.telegram_bot.views import get_text
from datetime import datetime


# Create your views here

def contact(request):
    info_contact = Contacts.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone')
        subject = request.POST.get('subject')
        description = request.POST.get('message')

        contacts = Contact.objects.create(
                name=name, 
                email=email, 
                number=number, 
                subject=subject,
                description=description
            )
          
        get_text(f"""
                Оставлена заявка на Обратный бронь 

Дата:  {datetime.now()}
Имя пользователя:  {name}
Почта пользователя: {email}
Номер телефона:  {number}
тема: {subject}
Сообщение: {description}
""")

    return render(request, 'base/contact.html', {'info_contact': info_contact})




from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import Reservation  # Подставьте свою модель Reservation
from datetime import datetime


def reservation(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            date = request.POST.get('date')
            time = request.POST.get('time')
            num_people = request.POST.get('num_people')

            # Преобразование даты и времени в нужный формат
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            time_obj = datetime.strptime(time, '%H:%M').time()

            # Создание нового объекта Reservation и сохранение его в базе данных
            reservation = Reservation.objects.create(
                name=name,
                email=email,
                phone=phone,
                date=date_obj,
                time=time_obj,
                num_people=num_people
            )

            # Отправка текстового сообщения
            message = f"""
            Оставлена заявка на бронирование столика:

            Дата: {datetime.now()}
            Имя пользователя: {name}
            Почта пользователя: {email}
            Номер телефона: {phone}
            Дата бронирования: {date} {time}
            Количество человек: {num_people}
            """
            get_text(message)

            # Возвращаем страницу с подтверждением бронирования
            return render(request, 'booking_confirmation.html', {'reservation': reservation})

        except Exception as e:
            return HttpResponseBadRequest(f'Ошибка при добавлении бронирования: {e}')

    # Если метод запроса GET, просто отображаем форму бронирования
    return render(request, 'reservation.html')

def booking_confirmation(request):
    return render(request, 'booking_confirmation.html', locals())