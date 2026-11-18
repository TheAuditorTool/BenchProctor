// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"encoding/json"
	"net/http"
	"strconv"
)

func BenchmarkTest00579(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	form := submissionForm{payload: jsonValue}
	data := form.payload
	tokenLen, _ := strconv.Atoi(data)
	if tokenLen < 16 || tokenLen > 64 {
		tokenLen = 32
	}
	buf := make([]byte, tokenLen)
	rand.Read(buf)
	RespondJSON(w, http.StatusOK, map[string]string{"token": hex.EncodeToString(buf)})
}
