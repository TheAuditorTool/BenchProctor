# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest49744(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
