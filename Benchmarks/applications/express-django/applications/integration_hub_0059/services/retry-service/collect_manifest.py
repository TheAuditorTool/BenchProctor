# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def collect_manifest(request):
    synopsis = request.body.decode('utf-8')
    handshake = synopsis if synopsis else 'default'
    parsed = yaml.safe_load(handshake)
    return JsonResponse({'parsed': str(parsed)}, status=200)
