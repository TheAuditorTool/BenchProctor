// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"html/template"
	"net/http"
	"regexp"
	"strings"
)

func BenchmarkTest00190(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	headerValue := r.Header.Get("X-Custom-Header")
	segments := strings.Split(headerValue, ",")
	data := strings.Join(segments, " ")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	bioTmpl := template.Must(template.New("bio").Parse(`<section class="bio">{{.}}</section>`))
	var bioPage bytes.Buffer
	if err := bioTmpl.Execute(&bioPage, template.HTML(processed)); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(bioPage.Bytes())
}
