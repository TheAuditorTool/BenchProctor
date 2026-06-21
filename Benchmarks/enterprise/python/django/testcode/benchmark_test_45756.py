# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest45756(request):
    raw_body = request.body.decode('utf-8')
    return HttpResponse('<!-- diagnostic build token: ' + str(raw_body) + ' -->', content_type='text/html')
