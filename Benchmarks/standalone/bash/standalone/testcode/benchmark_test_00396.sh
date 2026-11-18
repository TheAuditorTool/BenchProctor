#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00396() {
  user_input="$HTTP_X_FORWARDED_FOR"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  echo -n "$data" | sha256sum
}

benchmark_test_00396 "$@"
