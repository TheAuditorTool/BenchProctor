// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
)

func BenchmarkTest00116(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(headerValue)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
