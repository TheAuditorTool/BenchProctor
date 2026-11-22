# SPDX-License-Identifier: Apache-2.0
import html
from django.http import HttpResponse
from django.template import Template, Context


def BenchmarkTest00201(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    processed = html.escape(data)
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(processed)}))
    return HttpResponse(page)
