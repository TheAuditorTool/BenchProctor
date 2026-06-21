# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from django.http import HttpResponse


def BenchmarkTest45824(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
