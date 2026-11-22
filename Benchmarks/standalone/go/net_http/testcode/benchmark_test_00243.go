// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"html/template"
	"net/http"
	"strings"
)

func BenchmarkTest00243(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := func(v string) string { return strings.TrimSpace(v) }(refererValue)
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(w, "<p>Results for %s</p>", template.HTMLEscapeString(data))
}
