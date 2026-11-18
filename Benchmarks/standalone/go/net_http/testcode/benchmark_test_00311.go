// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00311(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	segments := strings.Split(rawBody, ",")
	data := strings.Join(segments, " ")
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+data+"']")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
