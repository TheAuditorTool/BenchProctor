// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00296(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	originValue := r.Header.Get("Origin")
	segments := strings.Split(originValue, ",")
	data := strings.Join(segments, " ")
	w.Header().Set("Location", data)
	w.WriteHeader(http.StatusSeeOther)
}
