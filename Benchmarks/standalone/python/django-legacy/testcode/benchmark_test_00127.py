# SPDX-License-Identifier: Apache-2.0
import base64
from django.http import HttpResponse
from django.template import Template, Context


def BenchmarkTest00127(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(data)}))
    return HttpResponse(page)
