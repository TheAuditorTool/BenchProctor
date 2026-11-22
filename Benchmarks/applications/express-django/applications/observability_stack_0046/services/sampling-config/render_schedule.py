# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def render_schedule(request):
    paragraph = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(paragraph)
    if gauge not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    cohort = gauge
    os.system('echo ' + str(cohort))
    return JsonResponse({"saved": True})
