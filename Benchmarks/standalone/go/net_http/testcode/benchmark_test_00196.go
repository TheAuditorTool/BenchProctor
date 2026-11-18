// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net"
	"net/http"
	"strings"
)

func BenchmarkTest00196(w http.ResponseWriter, r *http.Request) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	var data string
	for _, token := range strings.Split(redisValue, ",") {
		data = token
	}
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
