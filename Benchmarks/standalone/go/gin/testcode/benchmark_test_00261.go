// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00261(c *gin.Context) {
	fieldValue := c.PostForm("field")
	var data string
	if len(fieldValue) > 0 {
		data = fieldValue
	} else {
		data = "default"
	}
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
