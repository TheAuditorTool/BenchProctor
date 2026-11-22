// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"net/url"
)

func BenchmarkTest00256(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	data, _ := url.QueryUnescape(userID)
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(w, "<p>Results for %s</p>", data)
}
