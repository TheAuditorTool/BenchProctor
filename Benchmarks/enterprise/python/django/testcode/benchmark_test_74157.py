# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest74157(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
