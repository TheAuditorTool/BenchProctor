// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"net/http"
	"strings"

	"github.com/yuin/goldmark"
)

func BenchmarkTest00077(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	data := func(v string) string { return strings.TrimSpace(v) }(uaValue)
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
