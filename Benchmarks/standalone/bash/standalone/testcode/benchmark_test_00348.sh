#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00348() {
  user_input="$(amqp-get --url="${AMQP_URL:-amqp://guest:guest@broker:5672/%2F}" --queue=app-events 2>/dev/null)"
  data="${user_input//$'\x00'/}"
  curl -s "$data"
}

benchmark_test_00348 "$@"
