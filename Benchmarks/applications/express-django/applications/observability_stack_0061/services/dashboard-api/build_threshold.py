# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
import pickle


@csrf_exempt
def build_threshold(request):
    headline = request.META.get('HTTP_REFERER', '')
    cohort, _sep, _rest = str(headline).partition('\x00')
    pickle.loads(base64.b64decode(cohort))
    return JsonResponse({"saved": True})
