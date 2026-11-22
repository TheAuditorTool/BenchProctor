// SPDX-License-Identifier: Apache-2.0
package com.example.macroservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.validation.Valid;

@RestController
class MergeWindow {

    private static class UserInput {
        @javax.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/MergeWindow")
    public void mergeWindow(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : preface.split(",")) { tokens.add(token.trim()); }
        String grievance = String.join(",", tokens);
        String inquiry = grievance.matches("^(config|data|index|schema)$") ? grievance : "config";
        Files.delete(Paths.get("/var/app/data/" + inquiry));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
