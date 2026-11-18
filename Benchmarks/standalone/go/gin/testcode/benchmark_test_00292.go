// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00292(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	data := strings.ReplaceAll(multipartValue, "\x00", "")
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
