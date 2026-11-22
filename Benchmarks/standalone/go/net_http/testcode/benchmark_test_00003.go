// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/json"
	"net/http"
	"strings"
)

func BenchmarkTest00003(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	relayPrefix := ""
	if len(jsonValue) > 0 {
		relayPrefix = strings.ToLower(jsonValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = jsonValue
	case "f":
		data = jsonValue
	default:
		data = jsonValue
	}
	redisClient.HSet(context.Background(), "session:"+ctxString(r, ctxKeyUser), map[string]any{"display_name": data, "locale": "en"})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
