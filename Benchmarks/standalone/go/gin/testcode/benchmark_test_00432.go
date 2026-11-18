// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00432(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", originValue)
	data := relayBuilder.String()
	c.Redirect(http.StatusFound, data)
}
