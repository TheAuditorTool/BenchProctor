# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest34268(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
