// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"fmt"
	"net/http"

	mdparser "github.com/yuin/goldmark/v2/parser"
	mdhtml "github.com/yuin/goldmark/v2/renderer/html"
)

func BenchmarkTest00158(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	var data string
	if uaValue != "" {
		data = uaValue
	}
	var mdBuf bytes.Buffer
	mdSource := []byte(data)
	_ = mdhtml.New().Render(&mdBuf, mdSource, mdparser.New().Parse(mdSource))
	processed := mdBuf.String()
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(w, "<p>Results for %s</p>", processed)
}
