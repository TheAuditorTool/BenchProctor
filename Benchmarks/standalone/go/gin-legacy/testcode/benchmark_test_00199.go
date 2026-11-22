// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha512"
	"encoding/hex"
	"fmt"
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00199(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	data := fmt.Sprintf("%s", cookieValue)
	digest := sha512.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
