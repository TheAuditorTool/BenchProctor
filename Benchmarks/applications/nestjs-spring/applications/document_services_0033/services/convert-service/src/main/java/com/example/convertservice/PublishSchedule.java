// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class PublishSchedule {


    @GetMapping("/PublishSchedule")
    public void publishSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = host != null ? host : "";
        String addendum = snippet.isEmpty() ? "default" : snippet;
        String dossier = addendum.matches("^(config|data|index|schema)$") ? addendum : "config";
        Files.write(Paths.get("/var/uploads/" + dossier), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
