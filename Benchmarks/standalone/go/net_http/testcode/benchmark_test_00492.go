// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00492(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	data := strings.Join(strings.FieldsFunc(rawBody, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
