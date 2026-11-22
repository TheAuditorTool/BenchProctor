// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha1"
	"encoding/hex"
	"io"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00193(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	data := strings.ReplaceAll(multipartValue, "\x00", "")
	digest := sha1.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
