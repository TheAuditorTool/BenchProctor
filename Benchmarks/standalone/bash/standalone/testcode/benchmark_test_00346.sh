#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00346() {
  user_input="$USER_COMMENT"
  checked_path=$(realpath -m "/var/app/data/$user_input")
  if [[ ! "$checked_path" == /var/app/data/* ]]; then echo "forbidden" >&2; exit 1; fi
  rm -f "$checked_path"
}

benchmark_test_00346 "$@"
