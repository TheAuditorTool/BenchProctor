// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00260(c *gin.Context) {
	fieldValue := c.PostForm("field")
	data := strings.Join(strings.FieldsFunc(fieldValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
