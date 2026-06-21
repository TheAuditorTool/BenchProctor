# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django.http import HttpResponse
import unicodedata


def BenchmarkTest81056(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
