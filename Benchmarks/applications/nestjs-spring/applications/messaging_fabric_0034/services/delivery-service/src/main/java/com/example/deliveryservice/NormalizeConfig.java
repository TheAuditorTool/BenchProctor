// SPDX-License-Identifier: Apache-2.0
package com.example.deliveryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class NormalizeConfig {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/NormalizeConfig")
    public void normalizeConfig(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = sessionToken != null ? sessionToken : "";
        String bulletin = normalize(footnote);
        String heading = bulletin.matches("^(config|data|index|schema)$") ? bulletin : "config";
        Files.delete(Paths.get("/var/app/data/" + heading));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
