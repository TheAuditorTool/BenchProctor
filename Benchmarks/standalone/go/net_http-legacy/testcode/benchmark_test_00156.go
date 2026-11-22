// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
	"regexp"
)

func BenchmarkTest00156(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadedName := header.Filename
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(uploadedName) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := uploadedName
	ioutil.WriteFile("/var/app/data/"+processed, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
