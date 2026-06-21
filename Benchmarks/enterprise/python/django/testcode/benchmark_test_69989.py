# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest69989(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    reader = make_reader(origin_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
