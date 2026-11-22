// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.validation.Valid;

@RestController
class PublishConnector {

    private static class UserInput {
        @javax.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/PublishConnector")
    public void publishConnector(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : wording.split(",")) { tokens.add(token.trim()); }
        String handshake = String.join(",", tokens);
        String subject = handshake.matches("^(config|data|index|schema)$") ? handshake : "config";
        Files.delete(Paths.get("/var/app/data/" + subject));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
