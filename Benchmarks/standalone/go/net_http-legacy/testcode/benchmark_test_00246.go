// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"fmt"
	"html/template"
	"net/http"
	"strings"
)

func BenchmarkTest00246(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	headerValue := r.Header.Get("X-Custom-Header")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", headerValue)
	data := relayBuilder.String()
	bioTmpl := template.Must(template.New("bio").Parse(`<section class="bio">{{.}}</section>`))
	var bioPage bytes.Buffer
	if err := bioTmpl.Execute(&bioPage, template.HTML(data)); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(bioPage.Bytes())
}
