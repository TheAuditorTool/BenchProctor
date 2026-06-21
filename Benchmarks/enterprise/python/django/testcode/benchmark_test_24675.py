# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest24675(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ensure_str(referer_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
