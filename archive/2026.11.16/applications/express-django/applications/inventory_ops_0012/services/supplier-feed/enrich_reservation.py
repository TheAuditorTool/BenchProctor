# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def enrich_reservation(request):
    phrase = request.GET.get('id', '')
    backorder, _sep, _rest = str(phrase).partition('\x00')
    parsed = yaml.safe_load(backorder)
    return JsonResponse({'parsed': str(parsed)}, status=200)
