# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def BenchmarkTest05313(request):
    user_id = request.GET.get('id', '')
    with open(os.path.join('/var/app/data', str(user_id)), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
