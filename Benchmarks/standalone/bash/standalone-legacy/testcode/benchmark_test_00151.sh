#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00151() {
  user_input="$HTTP_AUTHORIZATION"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  printf '%s' "$data" | openssl dgst -md4 -provider legacy -provider default
}

benchmark_test_00151 "$@"
