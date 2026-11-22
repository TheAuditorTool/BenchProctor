// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"html/template"
	"io/ioutil"
	"net/http"
	"strings"
)

func BenchmarkTest00096(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	rawBytes, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	capture := func() string { return strings.TrimSpace(rawBody) }
	data := capture()
	bioTmpl := template.Must(template.New("bio").Parse(`<section class="bio">{{.}}</section>`))
	var bioPage bytes.Buffer
	if err := bioTmpl.Execute(&bioPage, template.HTML(data)); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(bioPage.Bytes())
}
