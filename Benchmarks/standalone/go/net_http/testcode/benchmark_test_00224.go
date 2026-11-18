// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"io"
	"net/http"
	"strings"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/sqs"
)

func BenchmarkTest00224(w http.ResponseWriter, r *http.Request) {
	var msgValue string
	_sqsOut, _sqsErr := sqsClient.ReceiveMessage(context.Background(), &sqs.ReceiveMessageInput{
		QueueUrl:            aws.String("https://sqs.us-east-1.amazonaws.com/123456789012/app-events"),
		MaxNumberOfMessages: 1,
	})
	if _sqsErr == nil && len(_sqsOut.Messages) > 0 {
		msgValue = aws.ToString(_sqsOut.Messages[0].Body)
	}
	data := msgValue
	if _, after, ok := strings.Cut(msgValue, ","); ok {
		data = after
	}
	resp, err := http.Get(data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	w.Write(body)
}
