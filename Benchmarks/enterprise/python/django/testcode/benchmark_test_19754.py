# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def BenchmarkTest19754(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
