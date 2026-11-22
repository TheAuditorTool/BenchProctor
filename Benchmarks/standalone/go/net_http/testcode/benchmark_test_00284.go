// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
)

func BenchmarkTest00284(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := fmt.Sprintf("%s", refererValue)
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(w, "<p>Results for %s</p>", data)
}
