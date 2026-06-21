# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from django.http import HttpResponse
import unicodedata


def BenchmarkTest46442(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
