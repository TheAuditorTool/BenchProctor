// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"

	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/sha3"
)

func BenchmarkTest00146(c *gin.Context) {
	userID := c.Query("id")
	var data string
	if len(userID) > 0 {
		data = userID
	} else {
		data = "default"
	}
	strongDigest := sha3.New256()
	strongDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(strongDigest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
