// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"net/http"
	"strings"

	"github.com/yuin/goldmark"
)

func BenchmarkTest00026(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	data := func(v string) string { return strings.TrimSpace(v) }(userID)
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
