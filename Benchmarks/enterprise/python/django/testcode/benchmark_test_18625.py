# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import re


def BenchmarkTest18625(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', cookie_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = cookie_value
    return HttpResponse(Template(processed).render(Context()))
