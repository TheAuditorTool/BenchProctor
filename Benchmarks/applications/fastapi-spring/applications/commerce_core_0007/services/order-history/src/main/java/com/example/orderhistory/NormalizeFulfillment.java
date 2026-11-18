// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import jakarta.validation.Valid;

@RestController
class NormalizeFulfillment {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/NormalizeFulfillment")
    public void normalizeFulfillment(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = req.payload;
        String voucher;
        try { voucher = String.valueOf(Integer.parseInt(heading)); }
        catch (NumberFormatException e) { voucher = heading; }
        byte[] serBytes = java.util.Base64.getDecoder().decode(voucher);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
