# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def reconcile_config(request):
    headline = request.body.decode('utf-8')
    disbursement = headline if headline else 'default'
    parsed = yaml.safe_load(disbursement)
    return JsonResponse({'parsed': str(parsed)}, status=200)
