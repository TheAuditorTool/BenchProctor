// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"html"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00028(c *gin.Context) {
	pathValue := c.Param("id")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", pathValue)
	data := relayBuilder.String()
	processed := html.EscapeString(data)
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
