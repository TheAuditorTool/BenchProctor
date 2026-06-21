# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest75355(request):
    multipart_value = request.POST.get('multipart_field', '')
    return HttpResponse('<script src="' + str(multipart_value) + '"></script>', content_type='text/html')
