// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class MergeProfile {


    @GetMapping("/MergeProfile")
    public void mergeProfile(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subtitle = origin != null ? origin : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(subtitle.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String ledger = String.join(",", lowered);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(ledger).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String remittance = resolved.toString();
        Files.write(Paths.get(remittance), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
