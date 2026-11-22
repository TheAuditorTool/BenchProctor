// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00005(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	forwardedIP := r.Header.Get("X-Forwarded-For")
	segments := strings.Split(forwardedIP, ",")
	data := strings.Join(segments, " ")
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
