// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00457(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var data string
	if authHeader != "" {
		data = authHeader
	}
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
