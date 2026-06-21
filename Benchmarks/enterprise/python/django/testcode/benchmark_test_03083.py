# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest03083(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
