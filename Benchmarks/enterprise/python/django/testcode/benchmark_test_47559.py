# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest47559(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    return HttpResponse(Template(data).render(Context()))
