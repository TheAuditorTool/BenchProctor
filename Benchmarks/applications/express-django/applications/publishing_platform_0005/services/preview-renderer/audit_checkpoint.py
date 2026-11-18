# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def audit_checkpoint(request):
    footnote = request.META.get('HTTP_AUTHORIZATION', '')
    kind = 'json' if str(footnote).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            byline = str(footnote).strip()
        case _:
            byline = str(footnote)
    os.unlink('/var/app/data/' + str(byline))
    return JsonResponse({"saved": True})
