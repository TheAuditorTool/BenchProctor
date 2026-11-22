// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand/v2"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00212(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	var data string
	if uaValue != "" {
		data = uaValue
	}
	otpValue := rand.Int32N(1000000)
	otpCode := fmt.Sprintf("%06d", otpValue)
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	c.JSON(http.StatusOK, map[string]string{"status": "challenge_sent"})
}
