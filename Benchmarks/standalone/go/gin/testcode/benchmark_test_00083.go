// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00083(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	form := submissionForm{payload: multipartValue}
	data := form.payload
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
