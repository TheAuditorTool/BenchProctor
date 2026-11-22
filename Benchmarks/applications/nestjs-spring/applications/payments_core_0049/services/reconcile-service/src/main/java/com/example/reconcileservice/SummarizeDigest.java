// SPDX-License-Identifier: Apache-2.0
package com.example.reconcileservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class SummarizeDigest {


    @GetMapping("/SummarizeDigest")
    public void summarizeDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = host != null ? host : "";
        String disbursement = headline.isEmpty() ? "default" : headline;
        String remittance = disbursement.matches("^(config|data|index|schema)$") ? disbursement : "config";
        Files.write(Paths.get("/var/uploads/" + remittance), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
