# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


@csrf_exempt
def normalize_policy(request):
    note = request.POST.get('multipart_field', '')
    kind = 'json' if str(note).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            cohort = str(note).strip()
        case _:
            cohort = str(note)
    requests.get(str(cohort))
    return JsonResponse({"saved": True})
