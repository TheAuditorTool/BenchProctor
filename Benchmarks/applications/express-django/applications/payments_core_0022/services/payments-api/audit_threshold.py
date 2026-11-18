# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def audit_threshold(request):
    subject = request.body.decode('utf-8')
    ledger = subject if subject else 'default'
    parsed = yaml.safe_load(ledger)
    return JsonResponse({'parsed': str(parsed)}, status=200)
