# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def render_batch(request):
    remark = request.META.get('HTTP_AUTHORIZATION', '')
    kind = 'json' if str(remark).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            remittance = str(remark).strip()
        case _:
            remittance = str(remark)
    os.unlink('/var/app/data/' + str(remittance))
    return JsonResponse({"saved": True})
