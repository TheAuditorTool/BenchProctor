// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"net/http"
	"strings"
)

func BenchmarkTest00193(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	data := strings.Join(strings.FieldsFunc(uaValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	apiToken := rand.Text()
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	RespondJSON(w, http.StatusOK, map[string]string{"token": apiToken})
}
