// SPDX-License-Identifier: Apache-2.0
package com.example.paymentgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class CapturePayment {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("billing_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/CapturePayment")
    public void capturePayment(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String arrears = inboundPayload.value != null ? inboundPayload.value : "";
        byte[] serBytes = java.util.Base64.getDecoder().decode(arrears);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
