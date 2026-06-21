# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest49644(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
