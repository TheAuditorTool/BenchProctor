# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest75350(request):
    xml_value = request.body.decode('utf-8')
    data = to_text(xml_value)
    processed = data[:64]
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
