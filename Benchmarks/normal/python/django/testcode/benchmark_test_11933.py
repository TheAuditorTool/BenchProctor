# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def BenchmarkTest11933(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
