# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def BenchmarkTest01062(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    normalized = unicodedata.normalize('NFKC', str(referer_value))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
