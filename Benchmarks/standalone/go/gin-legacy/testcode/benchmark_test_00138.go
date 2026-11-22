// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha1"
	"encoding/hex"
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00138(c *gin.Context) {
	fieldValue := c.PostForm("field")
	var data string
	if fieldValue != "" {
		data = fieldValue
	}
	digest := sha1.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
