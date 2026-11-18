// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00391(c *gin.Context) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	data := strings.Join(strings.FieldsFunc(redisValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
