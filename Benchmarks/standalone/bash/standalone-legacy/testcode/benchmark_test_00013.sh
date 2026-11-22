#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00013() {
  user_input="$HTTP_AUTHORIZATION"
  data="${user_input//$'\x00'/}"
  printf '%s' "$data" | openssl dgst -sha3-256
}

benchmark_test_00013 "$@"
