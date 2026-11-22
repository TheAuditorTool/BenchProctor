// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"fmt"
	"math/big"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00253(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	capture := func() string { return strings.TrimSpace(multipartValue) }
	data := capture()
	otpValue, err := rand.Int(rand.Reader, big.NewInt(1000000))
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	otpCode := fmt.Sprintf("%06d", otpValue.Int64())
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	c.JSON(http.StatusOK, map[string]string{"status": "challenge_sent"})
}
