// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00233(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	data := multipartValue
	if _, after, ok := strings.Cut(multipartValue, ","); ok {
		data = after
	}
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
