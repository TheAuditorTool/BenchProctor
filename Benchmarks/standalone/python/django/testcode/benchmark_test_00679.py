# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def BenchmarkTest00679(request):
    field_value = request.POST.get('field', '')
    data = '{}'.format(field_value)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
