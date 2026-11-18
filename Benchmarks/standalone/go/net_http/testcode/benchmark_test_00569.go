// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
)

func BenchmarkTest00569(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	os.Remove("/var/app/data/" + forwardedIP)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
