# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def merge_digest(request):
    excerpt = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    cohort = normalize(excerpt)
    if cohort not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    gauge = cohort
    os.system('echo ' + str(gauge))
    return JsonResponse({"saved": True})
