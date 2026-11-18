// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
)

func BenchmarkTest00011(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	var data string
	if len(originValue) > 0 {
		data = originValue
	} else {
		data = "default"
	}
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
