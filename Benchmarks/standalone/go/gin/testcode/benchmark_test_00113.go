// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00113(c *gin.Context) {
	pathValue := c.Param("id")
	relayPrefix := ""
	if len(pathValue) > 0 {
		relayPrefix = strings.ToLower(pathValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = pathValue
	case "f":
		data = pathValue
	default:
		data = pathValue
	}
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
