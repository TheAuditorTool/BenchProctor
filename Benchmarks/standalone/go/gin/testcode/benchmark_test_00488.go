// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00488(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	data := strings.Join(strings.FieldsFunc(forwardedIP, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
