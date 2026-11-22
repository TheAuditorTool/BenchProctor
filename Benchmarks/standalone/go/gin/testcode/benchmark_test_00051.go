// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/md4"
)

func BenchmarkTest00051(c *gin.Context) {
	hostValue := c.Request.Host
	data := hostValue
	if _, after, ok := strings.Cut(hostValue, ","); ok {
		data = after
	}
	legacyDigest := md4.New()
	legacyDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(legacyDigest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
