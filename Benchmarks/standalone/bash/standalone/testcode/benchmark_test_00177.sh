#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00177() {
  user_input="$HTTP_COOKIE"
  data="${user_input//$'\x00'/}"
  eval "echo $data"
}

benchmark_test_00177 "$@"
