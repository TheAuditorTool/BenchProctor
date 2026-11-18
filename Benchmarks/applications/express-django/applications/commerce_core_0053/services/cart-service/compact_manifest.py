# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def compact_manifest(request):
    memo = request.body.decode('utf-8')
    voucher = memo if memo else 'default'
    parsed = yaml.safe_load(voucher)
    return JsonResponse({'parsed': str(parsed)}, status=200)
