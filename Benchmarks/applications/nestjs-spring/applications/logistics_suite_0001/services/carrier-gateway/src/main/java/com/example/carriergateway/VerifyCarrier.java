// SPDX-License-Identifier: Apache-2.0
package com.example.carriergateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import jakarta.validation.Valid;

@RestController
class VerifyCarrier {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/VerifyCarrier")
    public void verifyCarrier(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String quotation = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : quotation.split(",")) { tokens.add(token.trim()); }
        String parcel = String.join(",", tokens);
        String consignment = parcel.matches("^(config|data|index|schema)$") ? parcel : "config";
        Files.delete(Paths.get("/var/app/data/" + consignment));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
