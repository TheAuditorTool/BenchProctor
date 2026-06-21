# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest21915(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = cookie_value
    return HttpResponse(Template(processed).render(Context()))
