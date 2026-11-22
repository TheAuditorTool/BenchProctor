// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00268(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	capture := func() string { return strings.TrimSpace(multipartValue) }
	data := capture()
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
