# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest74855(request):
    upload_name = request.FILES['upload'].name
    return HttpResponse('<script src="' + str(upload_name) + '"></script>', content_type='text/html')
