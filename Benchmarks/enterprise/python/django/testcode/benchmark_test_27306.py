# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest27306(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
