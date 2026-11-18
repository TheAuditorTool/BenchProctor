// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00174(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	capture := func() string { return strings.TrimSpace(originValue) }
	data := capture()
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[data] {
		http.Error(w, "forbidden", http.StatusForbidden)
		return
	}
	checkedPath := "/var/app/data/" + data
	os.Remove(checkedPath)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
