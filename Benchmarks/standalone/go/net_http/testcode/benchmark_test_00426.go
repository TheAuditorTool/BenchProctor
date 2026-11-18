// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net"
	"net/http"
	"strings"
)

func BenchmarkTest00426(w http.ResponseWriter, r *http.Request) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	data := strings.Join(strings.FieldsFunc(redisValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
