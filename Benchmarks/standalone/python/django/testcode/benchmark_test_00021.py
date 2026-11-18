# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00021(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
