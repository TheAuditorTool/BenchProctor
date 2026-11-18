// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00031(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(multipartValue)
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
