// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
)

func BenchmarkTest00310(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(hostValue) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := hostValue
	os.Remove("/var/app/data/" + processed)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
