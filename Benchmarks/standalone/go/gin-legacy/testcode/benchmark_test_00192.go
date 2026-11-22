// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/md4"
)

func BenchmarkTest00192(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	data := strings.ReplaceAll(uaValue, "\x00", "")
	legacyDigest := md4.New()
	legacyDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(legacyDigest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
