# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest39584(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
