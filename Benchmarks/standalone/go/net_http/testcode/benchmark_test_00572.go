// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
)

func BenchmarkTest00572(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	content, err := os.ReadFile("/var/app/data/" + hostValue)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
