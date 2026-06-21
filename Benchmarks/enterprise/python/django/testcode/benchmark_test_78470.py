# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest78470(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    return HttpResponse(str(forwarded_ip), content_type='text/html')
