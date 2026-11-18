// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00169(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	var data string
	for _, token := range strings.Split(headerValue, ",") {
		data = token
	}
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
