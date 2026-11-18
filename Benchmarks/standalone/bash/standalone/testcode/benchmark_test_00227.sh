#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00227() {
  user_input="$HTTP_AUTHORIZATION"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  echo -n "$data" | md5sum
}

benchmark_test_00227 "$@"
