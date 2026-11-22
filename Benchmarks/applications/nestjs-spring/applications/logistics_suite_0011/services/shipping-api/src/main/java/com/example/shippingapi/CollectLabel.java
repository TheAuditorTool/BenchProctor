// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.validation.Valid;

@RestController
class CollectLabel {

    private static class UserInput {
        @javax.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/CollectLabel")
    public void collectLabel(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : citation.split(",")) { tokens.add(token.trim()); }
        String consignment = String.join(",", tokens);
        String parcel = consignment.matches("^(config|data|index|schema)$") ? consignment : "config";
        Files.delete(Paths.get("/var/app/data/" + parcel));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
