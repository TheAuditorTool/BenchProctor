# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def prune_header(request):
    memo = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    backorder = '%s' % (memo,)
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(backorder)}))
    return HttpResponse(page)
