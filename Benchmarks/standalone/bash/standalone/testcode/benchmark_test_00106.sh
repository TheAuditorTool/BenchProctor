#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00106() {
  user_input="$HTTP_ORIGIN"
  data="${user_input:-default}"
  checked_path=$(realpath -m "/var/app/data/$data")
  if [[ ! "$checked_path" == /var/app/data/* ]]; then echo "forbidden"; exit 1; fi
  rm -f "$checked_path"
}

benchmark_test_00106 "$@"
