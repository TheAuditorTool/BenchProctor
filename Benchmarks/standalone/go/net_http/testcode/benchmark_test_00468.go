// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
)

func BenchmarkTest00468(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(userID)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
