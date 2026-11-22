#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00051() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  reset_code="$RANDOM$RANDOM"
  echo "$reset_code"
}

benchmark_test_00051 "$@"
