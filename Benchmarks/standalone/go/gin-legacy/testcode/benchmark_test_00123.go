// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/sha3"
)

func BenchmarkTest00123(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	data := strings.ReplaceAll(forwardedIP, "\x00", "")
	strongDigest := sha3.New256()
	strongDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(strongDigest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
