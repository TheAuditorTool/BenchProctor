# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def to_text(value):
    return str(value).strip()

def BenchmarkTest03608(request):
    xml_value = request.body.decode('utf-8')
    data = to_text(xml_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
