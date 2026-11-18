// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00359(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	pending := strings.Split(multipartValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+data+"']")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
