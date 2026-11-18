// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00470(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", authHeader)
	data := relayBuilder.String()
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
