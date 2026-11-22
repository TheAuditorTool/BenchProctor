# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def render_conversion(request):
    snippet = request.POST.get('field', '')
    addendum = (lambda v: v.strip())(snippet)
    if addendum not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    dossier = addendum
    os.system('echo ' + str(dossier))
    return JsonResponse({"saved": True})
