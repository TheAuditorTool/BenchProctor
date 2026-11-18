// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00414(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	htmlOut := "<div>" + authHeader + "</div>"
	w.Write([]byte(htmlOut))
}
