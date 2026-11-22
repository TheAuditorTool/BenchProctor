// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha3"
	"encoding/hex"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00263(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	form := submissionForm{payload: originValue}
	data := form.payload
	strongDigest := sha3.New256()
	strongDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(strongDigest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
