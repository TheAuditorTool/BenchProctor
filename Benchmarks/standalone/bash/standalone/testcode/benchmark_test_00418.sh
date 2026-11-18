#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00418() {
  user_input="$(amqp-get --url="${AMQP_URL:-amqp://guest:guest@broker:5672/%2F}" --queue=app-events 2>/dev/null)"
  data="${user_input//$'\x00'/}"
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00418 "$@"
