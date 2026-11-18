// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"io"
	"net/http"
	"regexp"
	"strings"
)

func BenchmarkTest00463(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	pending := strings.Split(xmlBody, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, processed))
}
