// SPDX-License-Identifier: Apache-2.0
package com.example.captureservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ReconcileDispute {


    @GetMapping("/ReconcileDispute")
    public void reconcileDispute(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = host != null ? host : "";
        String remittance = footnote.isEmpty() ? "default" : footnote;
        String disbursement = remittance.matches("^(config|data|index|schema)$") ? remittance : "config";
        Files.write(Paths.get("/var/uploads/" + disbursement), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
