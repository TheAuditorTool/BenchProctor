// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00040(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	rawBytes, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(xmlBody)
	orderDoc, parseErr := xmlquery.Parse(strings.NewReader(data))
	if parseErr != nil {
		http.Error(w, "malformed order", http.StatusBadRequest)
		return
	}
	totalNode := xmlquery.FindOne(orderDoc, "//order/total")
	if totalNode == nil {
		http.Error(w, "order total missing", http.StatusBadRequest)
		return
	}
	orderTotal := totalNode.InnerText()
	RespondJSON(w, http.StatusOK, map[string]string{"total": orderTotal})
}
