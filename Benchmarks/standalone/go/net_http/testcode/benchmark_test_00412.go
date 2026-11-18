// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00412(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", headerValue)
	data := relayBuilder.String()
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+data+"']")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
