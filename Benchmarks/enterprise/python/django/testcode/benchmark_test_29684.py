# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from django.http import HttpResponse


def BenchmarkTest29684(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
