#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00176() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data="${user_input//$'\x00'/}"
  checked_path=$(realpath -m "/var/app/data/$data")
  if [[ ! "$checked_path" == /var/app/data/* ]]; then echo "forbidden" >&2; exit 1; fi
  echo "data" > "$checked_path"
}

benchmark_test_00176 "$@"
