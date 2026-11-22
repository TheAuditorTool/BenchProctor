// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00098(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	segments := strings.Split(hostValue, ",")
	data := strings.Join(segments, " ")
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
