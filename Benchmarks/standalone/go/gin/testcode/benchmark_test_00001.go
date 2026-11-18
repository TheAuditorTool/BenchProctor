// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/json"
	"net"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00001(c *gin.Context) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	var parsed map[string]interface{}
	json.Unmarshal([]byte(redisValue), &parsed)
	data, _ := parsed["value"].(string)
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
