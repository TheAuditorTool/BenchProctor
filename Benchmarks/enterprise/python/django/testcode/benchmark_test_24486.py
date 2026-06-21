# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def BenchmarkTest24486(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
