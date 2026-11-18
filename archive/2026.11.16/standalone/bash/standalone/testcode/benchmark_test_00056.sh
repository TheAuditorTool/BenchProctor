#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00056() {
  user_input="$HTTP_AUTHORIZATION"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  checked_path=$(realpath -m "/var/app/data/$data")
  if [[ ! "$checked_path" == /var/app/data/* ]]; then echo "forbidden"; exit 1; fi
  echo "data" > "$checked_path"
}

benchmark_test_00056 "$@"
