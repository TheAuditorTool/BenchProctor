// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00482(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", refererValue)
	data := relayBuilder.String()
	c.Redirect(http.StatusFound, data)
}
