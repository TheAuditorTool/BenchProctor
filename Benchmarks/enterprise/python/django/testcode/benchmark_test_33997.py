# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest33997(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = ua_value
    return HttpResponse(Template(processed).render(Context()))
