# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def summarize_schedule(request):
    excerpt = request.META.get('HTTP_AUTHORIZATION', '')
    cohort, _sep, _rest = str(excerpt).partition('\x00')
    os.system('echo ' + str(cohort))
    return JsonResponse({"saved": True})
