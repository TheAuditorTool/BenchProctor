// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00376(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	relayPrefix := ""
	if len(fieldValue) > 0 {
		relayPrefix = strings.ToLower(fieldValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = fieldValue
	case "f":
		data = fieldValue
	default:
		data = fieldValue
	}
	_lower := strings.ToLower(data)
	if !strings.HasPrefix(_lower, "t") && !strings.HasPrefix(_lower, "f") && _lower != "1" && _lower != "0" {
		http.Error(w, "invalid boolean", http.StatusBadRequest)
		return
	}
	parsedBool := strconv.FormatBool(strings.HasPrefix(_lower, "t") || _lower == "1")
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, parsedBool))
}
