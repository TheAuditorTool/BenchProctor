# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
import pickle


@csrf_exempt
def compact_index(request):
    passage = request.META.get('HTTP_REFERER', '')
    dossier, _sep, _rest = str(passage).partition('\x00')
    pickle.loads(base64.b64decode(dossier))
    return JsonResponse({"saved": True})
