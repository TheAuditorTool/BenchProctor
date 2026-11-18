// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00559(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	var data string
	for _, token := range strings.Split(originValue, ",") {
		data = token
	}
	c.Set("data", data)
}
