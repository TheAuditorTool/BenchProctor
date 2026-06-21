# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest10801(request):
    xml_value = request.body.decode('utf-8')
    if xml_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = xml_value
    return HttpResponse(Template(processed).render(Context()))
