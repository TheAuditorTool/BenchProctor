# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import re


def normalise_input(value):
    return value.strip()

def BenchmarkTest47562(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = normalise_input(multipart_value)
    if not re.fullmatch('^[\\w\\s<>\\"\'/(){}.*]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
