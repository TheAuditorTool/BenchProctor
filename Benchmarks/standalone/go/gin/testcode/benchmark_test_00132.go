// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00132(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	capture := func() string { return strings.TrimSpace(originValue) }
	data := capture()
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
