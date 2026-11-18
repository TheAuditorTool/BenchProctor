// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
	"strings"
)

func BenchmarkTest00186(w http.ResponseWriter, r *http.Request) {
	var profileBio string
	DB.QueryRow("SELECT bio FROM profiles LIMIT 1").Scan(&profileBio)
	pending := strings.Split(profileBio, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.#~\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	os.Remove("/var/app/data/" + processed)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
