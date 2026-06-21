# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest07254(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    return HttpResponse(Template(data).render(Context()))
