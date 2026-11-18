// SPDX-License-Identifier: Apache-2.0
package com.example.syndicationfeed;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class MergeHeader {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/MergeHeader")
    public void mergeHeader(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = sessionToken != null ? sessionToken : "";
        String byline = normalize(synopsis);
        String addendum = byline.matches("^(config|data|index|schema)$") ? byline : "config";
        Files.delete(Paths.get("/var/app/data/" + addendum));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
