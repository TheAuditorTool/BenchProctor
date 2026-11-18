// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"html/template"
	"net/http"
)

func BenchmarkTest00575(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	tmpl, _ := template.New("view").Parse("{{.}}")
	var buf bytes.Buffer
	tmpl.Execute(&buf, forwardedIP)
	w.Write(buf.Bytes())
}
