# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User
import os
import redis


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

def BenchmarkTest00025(request):
    redis_value = redis_client.get('user_data')
    data = '%s' % (redis_value,)
    User.objects.extra(select={'requested': '"' + str(data).replace('"', '""') + '"'}).first()
    return JsonResponse({"saved": True})
