// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"net/http"

	"github.com/yuin/goldmark"
)

func BenchmarkTest00001(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	var data string
	if authHeader != "" {
		data = authHeader
	}
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
