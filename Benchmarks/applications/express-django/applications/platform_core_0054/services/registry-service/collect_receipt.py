# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def collect_receipt(request):
    snippet = request.body.decode('utf-8')
    persona = snippet if snippet else 'default'
    parsed = yaml.safe_load(persona)
    return JsonResponse({'parsed': str(parsed)}, status=200)
