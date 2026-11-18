// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00255(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", uaValue)
	data := relayBuilder.String()
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
