#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00134() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  data="${user_input//$'\x00'/}"
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00134 "$@"
