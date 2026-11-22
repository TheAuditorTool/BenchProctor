# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def render_caption(request):
    synopsis = request.META.get('HTTP_ORIGIN', '')
    rendition = f'{synopsis!s}'
    parsed = json.loads(rendition)
    return JsonResponse({'parsed': str(parsed)}, status=200)
