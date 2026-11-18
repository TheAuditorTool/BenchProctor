// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EnrichReservation {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/EnrichReservation")
    public void enrichReservation(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = sessionToken != null ? sessionToken : "";
        String backorder = normalize(phrase);
        String restock = backorder.matches("^(status|info|list|show)$") ? backorder : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + restock}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
