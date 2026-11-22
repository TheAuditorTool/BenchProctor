// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"net/http"
)

func BenchmarkTest00012(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	form := submissionForm{payload: headerValue}
	data := form.payload
	apiToken := rand.Text()
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	RespondJSON(w, http.StatusOK, map[string]string{"token": apiToken})
}
