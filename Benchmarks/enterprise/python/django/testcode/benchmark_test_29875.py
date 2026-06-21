# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def BenchmarkTest29875(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    normalized = unicodedata.normalize('NFKC', str(header_value))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
