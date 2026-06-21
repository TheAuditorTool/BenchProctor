# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest58378(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
