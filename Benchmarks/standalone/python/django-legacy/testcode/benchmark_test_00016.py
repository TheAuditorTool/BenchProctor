# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse
from django.template import Template, Context


def BenchmarkTest00016(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(processed)}))
    return HttpResponse(page)
