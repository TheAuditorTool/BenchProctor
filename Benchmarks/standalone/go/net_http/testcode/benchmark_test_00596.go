// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00596(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data, _ := url.QueryUnescape(refererValue)
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+data+"']")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
