#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00118() {
  user_input="`amqp-get --url="${AMQP_URL:-amqp://guest:guest@broker:5672/%2F}" --queue=app-events 2>/dev/null`"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00118 "$@"
