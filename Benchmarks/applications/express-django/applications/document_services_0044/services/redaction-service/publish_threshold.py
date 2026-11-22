# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import re


@csrf_exempt
def publish_threshold(request):
    phrase = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(phrase).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            dossier = str(phrase).strip()
        case _:
            dossier = str(phrase)
    if not re.fullmatch("^(asc|desc|name|created)$", str(dossier)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    addendum = dossier
    with open('/var/app/data/' + str(addendum), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
