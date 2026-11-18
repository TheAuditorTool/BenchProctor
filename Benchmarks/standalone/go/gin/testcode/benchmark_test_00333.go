// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00333(c *gin.Context) {
	fieldValue := c.PostForm("field")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", fieldValue)
	data := relayBuilder.String()
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
