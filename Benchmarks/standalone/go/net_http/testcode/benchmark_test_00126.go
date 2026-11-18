// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
)

func BenchmarkTest00126(w http.ResponseWriter, r *http.Request) {
	var profileBio string
	DB.QueryRow("SELECT bio FROM profiles LIMIT 1").Scan(&profileBio)
	var data string
	if profileBio != "" {
		data = profileBio
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	os.Remove("/var/app/data/" + processed)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
