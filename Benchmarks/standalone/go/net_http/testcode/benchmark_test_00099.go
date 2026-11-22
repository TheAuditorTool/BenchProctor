// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
)

func BenchmarkTest00099(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	content, err := os.ReadFile("/var/app/data/" + authHeader)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
