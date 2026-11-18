#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00372() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  checked_path=$(realpath -m "/var/app/data/$data")
  if [[ ! "$checked_path" == /var/app/data/* ]]; then echo "forbidden"; exit 1; fi
  echo "data" > "$checked_path"
}

benchmark_test_00372 "$@"
