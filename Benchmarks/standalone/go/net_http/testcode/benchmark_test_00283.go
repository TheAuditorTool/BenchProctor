// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
)

func BenchmarkTest00283(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	var data string
	if len(refererValue) > 0 {
		data = refererValue
	} else {
		data = "default"
	}
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
