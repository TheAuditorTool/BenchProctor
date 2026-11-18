// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import jakarta.validation.Valid;

@RestController
class RenderReceipt {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/RenderReceipt")
    public void renderReceipt(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = req.payload;
        String rendition;
        try { rendition = String.valueOf(Integer.parseInt(transcript)); }
        catch (NumberFormatException e) { rendition = transcript; }
        byte[] serBytes = java.util.Base64.getDecoder().decode(rendition);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
