// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand/v2"
	"net/http"
	"strings"
)

func BenchmarkTest00235(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	relayPrefix := ""
	if len(authHeader) > 0 {
		relayPrefix = strings.ToLower(authHeader[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = authHeader
	case "f":
		data = authHeader
	default:
		data = authHeader
	}
	otpValue := rand.Int32N(1000000)
	otpCode := fmt.Sprintf("%06d", otpValue)
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	RespondJSON(w, http.StatusOK, map[string]string{"status": "challenge_sent"})
}
