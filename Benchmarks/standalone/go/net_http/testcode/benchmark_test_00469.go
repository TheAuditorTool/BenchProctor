// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00469(w http.ResponseWriter, r *http.Request) {
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadName := header.Filename
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(uploadName)
	os.Remove("/var/app/data/" + data)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
