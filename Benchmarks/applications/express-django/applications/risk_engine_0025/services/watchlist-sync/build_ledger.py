# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def build_ledger(request):
    excerpt = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    verdict = normalize(excerpt)
    if verdict not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    grievance = verdict
    os.system('echo ' + str(grievance))
    return JsonResponse({"saved": True})
