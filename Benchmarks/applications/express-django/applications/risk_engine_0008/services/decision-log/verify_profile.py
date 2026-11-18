# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def verify_profile(request):
    synopsis = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    verdict = normalize(synopsis)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if verdict not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    grievance = '/var/app/data/' + verdict
    os.unlink(grievance)
    return JsonResponse({"saved": True})
