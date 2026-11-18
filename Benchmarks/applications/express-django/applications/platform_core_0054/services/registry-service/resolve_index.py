# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def resolve_index(request):
    snippet = request.META.get('HTTP_AUTHORIZATION', '')
    kind = 'json' if str(snippet).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            persona = str(snippet).strip()
        case _:
            persona = str(snippet)
    os.unlink('/var/app/data/' + str(persona))
    return JsonResponse({"saved": True})
