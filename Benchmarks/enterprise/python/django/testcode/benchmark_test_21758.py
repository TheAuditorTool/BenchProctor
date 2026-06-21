# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django.http import HttpResponse
import os


def BenchmarkTest21758(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
