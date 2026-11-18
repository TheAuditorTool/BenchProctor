// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00182(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	form := submissionForm{payload: multipartValue}
	data := form.payload
	os.Remove("/var/app/data/" + data)
	c.JSON(200, gin.H{"code": "OK"})
}
