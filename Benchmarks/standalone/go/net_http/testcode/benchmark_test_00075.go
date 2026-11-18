// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00075(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	capture := func() string { return strings.TrimSpace(fieldValue) }
	data := capture()
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		http.Error(w, "invalid number", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+boundedVal+"']")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
