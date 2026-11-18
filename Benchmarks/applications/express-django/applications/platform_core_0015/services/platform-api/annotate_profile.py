# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def annotate_profile(request):
    note = request.body.decode('utf-8')
    handshake = note if note else 'default'
    parsed = yaml.safe_load(handshake)
    return JsonResponse({'parsed': str(parsed)}, status=200)
