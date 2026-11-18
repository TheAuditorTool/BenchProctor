// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00229(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := func(v string) string { return strings.TrimSpace(v) }(refererValue)
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
