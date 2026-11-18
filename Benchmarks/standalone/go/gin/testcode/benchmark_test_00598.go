// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00598(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(uaValue)
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
