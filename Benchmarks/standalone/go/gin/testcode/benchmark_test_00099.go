// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00099(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	form := submissionForm{payload: multipartValue}
	data := form.payload
	c.Redirect(http.StatusFound, data)
}
