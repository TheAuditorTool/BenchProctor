// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00111(c *gin.Context) {
	userID := c.Query("id")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(userID)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
