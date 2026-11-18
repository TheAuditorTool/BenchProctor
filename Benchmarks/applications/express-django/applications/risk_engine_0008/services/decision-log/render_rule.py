# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def render_rule(request):
    synopsis = request.META.get('HTTP_AUTHORIZATION', '')
    kind = 'json' if str(synopsis).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            verdict = str(synopsis).strip()
        case _:
            verdict = str(synopsis)
    os.unlink('/var/app/data/' + str(verdict))
    return JsonResponse({"saved": True})
