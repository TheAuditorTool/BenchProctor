// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00163(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := fmt.Sprintf("%s", refererValue)
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
