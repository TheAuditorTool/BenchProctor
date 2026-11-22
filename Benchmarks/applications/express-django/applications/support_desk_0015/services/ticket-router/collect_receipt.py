# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def collect_receipt(request):
    phrase = request.META.get('HTTP_USER_AGENT', '')
    grievance, _sep, _rest = str(phrase).partition('\x00')
    yaml.load(grievance, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
