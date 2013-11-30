from django.shortcuts import render_to_response
import datetime

def home(request):
    return render_to_response(
            'bookstore/index.html',
            { 'clock': datetime.datetime.now() },
        )
