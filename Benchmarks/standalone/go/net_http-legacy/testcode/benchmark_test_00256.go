// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"html"
	"net/http"
	"strings"
)

func BenchmarkTest00256(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	headerValue := r.Header.Get("X-Custom-Header")
	data := func(v string) string { return strings.TrimSpace(v) }(headerValue)
	processed := html.EscapeString(data)
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(w, "<p>Results for %s</p>", processed)
}
