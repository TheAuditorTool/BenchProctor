// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00456(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	data := strings.ReplaceAll(headerValue, "\x00", "")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+processed+"']")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
