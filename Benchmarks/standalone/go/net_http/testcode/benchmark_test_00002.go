// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00002(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	relayPrefix := ""
	if len(dbValue) > 0 {
		relayPrefix = strings.ToLower(dbValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = dbValue
	case "f":
		data = dbValue
	default:
		data = dbValue
	}
	tokenLen, _ := strconv.Atoi(data)
	if tokenLen < 16 || tokenLen > 64 {
		tokenLen = 32
	}
	buf := make([]byte, tokenLen)
	rand.Read(buf)
	RespondJSON(w, http.StatusOK, map[string]string{"token": hex.EncodeToString(buf)})
}
