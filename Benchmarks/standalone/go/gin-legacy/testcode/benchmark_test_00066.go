// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"fmt"
	"math/big"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00066(c *gin.Context) {
	pathValue := c.Param("id")
	data := fmt.Sprintf("%s", pathValue)
	otpValue, err := rand.Int(rand.Reader, big.NewInt(1000000))
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	otpCode := fmt.Sprintf("%06d", otpValue.Int64())
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	c.JSON(http.StatusOK, map[string]string{"status": "challenge_sent"})
}
