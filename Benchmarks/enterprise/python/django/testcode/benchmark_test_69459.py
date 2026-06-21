# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def BenchmarkTest69459(request):
    raw_body = request.body.decode('utf-8')
    normalized = unicodedata.normalize('NFKC', str(raw_body))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
