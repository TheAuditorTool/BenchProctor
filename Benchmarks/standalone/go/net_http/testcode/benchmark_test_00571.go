// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/json"
	"net"
	"net/http"
)

func BenchmarkTest00571(w http.ResponseWriter, r *http.Request) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	var parsed map[string]interface{}
	json.Unmarshal([]byte(redisValue), &parsed)
	data, _ := parsed["value"].(string)
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
