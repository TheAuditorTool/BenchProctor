// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00062(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	segments := strings.Split(forwardedIP, ",")
	data := strings.Join(segments, " ")
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
