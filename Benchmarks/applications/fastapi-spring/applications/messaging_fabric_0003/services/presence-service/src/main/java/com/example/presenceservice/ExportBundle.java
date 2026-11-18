// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import jakarta.validation.Valid;

@RestController
class ExportBundle {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/ExportBundle")
    public void exportBundle(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = req.payload;
        String bulletin;
        try { bulletin = String.valueOf(Integer.parseInt(subject)); }
        catch (NumberFormatException e) { bulletin = subject; }
        byte[] serBytes = java.util.Base64.getDecoder().decode(bulletin);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
