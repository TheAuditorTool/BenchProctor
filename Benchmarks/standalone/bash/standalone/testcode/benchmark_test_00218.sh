#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00218() {
  user_input="$HTTP_USER_AGENT"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  checked_path=$(realpath -m "/var/app/data/$data")
  if [[ ! "$checked_path" == /var/app/data/* ]]; then echo "forbidden"; exit 1; fi
  rm -f "$checked_path"
}

benchmark_test_00218 "$@"
