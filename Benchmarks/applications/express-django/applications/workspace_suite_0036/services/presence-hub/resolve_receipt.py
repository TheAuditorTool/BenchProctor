# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


@csrf_exempt
def resolve_receipt(request):
    remark = request.META.get('HTTP_ORIGIN', '')
    kind = 'json' if str(remark).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            synopsis = str(remark).strip()
        case _:
            synopsis = str(remark)
    requests.get(str(synopsis))
    return JsonResponse({"saved": True})
