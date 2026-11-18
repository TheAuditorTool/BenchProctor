// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00140(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(headerValue)
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
