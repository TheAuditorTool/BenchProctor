// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os"
	"regexp"
	"strings"
)

func BenchmarkTest00155(w http.ResponseWriter, r *http.Request) {
	pathValue := strings.TrimPrefix(r.URL.Path, "/api/")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", pathValue)
	data := relayBuilder.String()
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	os.WriteFile("/var/app/data/"+processed, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
