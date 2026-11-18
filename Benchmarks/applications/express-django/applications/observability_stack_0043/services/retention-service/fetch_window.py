# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def fetch_window(request):
    note = request.body.decode('utf-8')
    gauge = note if note else 'default'
    parsed = yaml.safe_load(gauge)
    return JsonResponse({'parsed': str(parsed)}, status=200)
