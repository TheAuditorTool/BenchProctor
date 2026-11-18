// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
)

func BenchmarkTest00449(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	os.WriteFile("/var/app/data/"+fieldValue, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
