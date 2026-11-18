// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00289(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	data := strings.ReplaceAll(originValue, "\x00", "")
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
