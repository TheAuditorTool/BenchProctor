// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00027(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	data := func(v string) string { return strings.TrimSpace(v) }(uaValue)
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
