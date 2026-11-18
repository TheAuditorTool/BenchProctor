// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"os"
	"regexp"
	"strings"
)

func BenchmarkTest00068(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(xmlBody)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	os.Remove("/var/app/data/" + processed)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
