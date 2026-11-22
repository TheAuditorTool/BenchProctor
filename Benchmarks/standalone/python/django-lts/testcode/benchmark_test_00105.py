# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import Template, Context
import re


def BenchmarkTest00105(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(processed)}))
    return HttpResponse(page)
