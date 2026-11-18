// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
)

func BenchmarkTest00548(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	form := submissionForm{payload: uaValue}
	data := form.payload
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
