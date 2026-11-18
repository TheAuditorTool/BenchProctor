# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def render_snapshot(request):
    remark = request.body.decode('utf-8')
    remittance = remark if remark else 'default'
    parsed = yaml.safe_load(remittance)
    return JsonResponse({'parsed': str(parsed)}, status=200)
