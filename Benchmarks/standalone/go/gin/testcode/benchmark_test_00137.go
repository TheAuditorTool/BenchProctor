// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand/v2"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00137(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(forwardedIP)
	otpValue := rand.Int32N(1000000)
	otpCode := fmt.Sprintf("%06d", otpValue)
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	c.JSON(http.StatusOK, map[string]string{"status": "challenge_sent"})
}
