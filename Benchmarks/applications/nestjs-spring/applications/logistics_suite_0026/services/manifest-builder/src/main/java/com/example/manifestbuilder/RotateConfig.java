// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RotateConfig {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/RotateConfig")
    public void rotateConfig(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = sessionToken != null ? sessionToken : "";
        String parcel = normalize(citation);
        String consignment = parcel.matches("^(config|data|index|schema)$") ? parcel : "config";
        Files.delete(Paths.get("/var/app/data/" + consignment));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
