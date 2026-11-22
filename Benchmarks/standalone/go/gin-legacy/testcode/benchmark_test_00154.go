// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00154(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	data := strings.Join(strings.FieldsFunc(authHeader, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
