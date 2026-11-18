# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


def BenchmarkTest00107(request):
    field_value = request.POST.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
