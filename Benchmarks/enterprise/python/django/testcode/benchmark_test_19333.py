# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest19333(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
