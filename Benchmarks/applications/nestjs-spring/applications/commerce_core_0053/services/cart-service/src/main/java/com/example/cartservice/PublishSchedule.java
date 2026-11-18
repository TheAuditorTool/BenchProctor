// SPDX-License-Identifier: Apache-2.0
package com.example.cartservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class PublishSchedule {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/PublishSchedule")
    public void publishSchedule(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = sessionToken != null ? sessionToken : "";
        String voucher = normalize(memo);
        String backorder = voucher.matches("^(config|data|index|schema)$") ? voucher : "config";
        Files.delete(Paths.get("/var/app/data/" + backorder));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
