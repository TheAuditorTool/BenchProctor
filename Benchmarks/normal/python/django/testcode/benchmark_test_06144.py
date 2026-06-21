# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def normalise_input(value):
    return value.strip()

def BenchmarkTest06144(request):
    raw_body = request.body.decode('utf-8')
    data = normalise_input(raw_body)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
