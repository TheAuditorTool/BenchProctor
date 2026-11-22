// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00175(w http.ResponseWriter, r *http.Request) {
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadName := header.Filename
	data := func(v string) string { return strings.TrimSpace(v) }(uploadName)
	w.Header().Set("Location", data)
	w.WriteHeader(http.StatusSeeOther)
}
