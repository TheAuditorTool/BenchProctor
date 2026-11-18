// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00313(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	capture := func() string { return strings.TrimSpace(multipartValue) }
	data := capture()
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
