#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00170() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  checked_path=$(realpath -m "/var/app/data/$user_input")
  if [[ ! "$checked_path" == /var/app/data/* ]]; then echo "forbidden"; exit 1; fi
  rm -f "$checked_path"
}

benchmark_test_00170 "$@"
