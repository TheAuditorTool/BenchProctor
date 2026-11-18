// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00597(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", multipartValue)
	data := relayBuilder.String()
	c.Redirect(http.StatusFound, data)
}
