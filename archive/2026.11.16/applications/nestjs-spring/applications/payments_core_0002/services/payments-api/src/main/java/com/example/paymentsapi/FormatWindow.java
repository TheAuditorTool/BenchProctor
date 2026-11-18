// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class FormatWindow {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/FormatWindow")
    public void formatWindow(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subtitle = java.util.Optional.ofNullable(System.getenv("PAYMENTS_INPUT_0002")).orElse("");
        String ledger = normalize(subtitle);
        Files.delete(Paths.get("/var/app/data/" + ledger));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
