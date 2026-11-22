// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"html"
	"html/template"
	"net/http"
	"strings"
)

func BenchmarkTest00037(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	fieldValue := r.FormValue("field")
	data := strings.Join(strings.FieldsFunc(fieldValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	processed := html.EscapeString(data)
	bioTmpl := template.Must(template.New("bio").Parse(`<section class="bio">{{.}}</section>`))
	var bioPage bytes.Buffer
	if err := bioTmpl.Execute(&bioPage, template.HTML(processed)); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(bioPage.Bytes())
}
