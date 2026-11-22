// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"html"
	"net/http"
	"strings"
)

func BenchmarkTest00096(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	capture := func() string { return strings.TrimSpace(refererValue) }
	data := capture()
	processed := html.EscapeString(data)
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(w, "<p>Results for %s</p>", processed)
}
