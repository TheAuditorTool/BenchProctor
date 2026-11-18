# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
from django.template import Template, Context


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00254(request):
    cookie_value = request.COOKIES.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
