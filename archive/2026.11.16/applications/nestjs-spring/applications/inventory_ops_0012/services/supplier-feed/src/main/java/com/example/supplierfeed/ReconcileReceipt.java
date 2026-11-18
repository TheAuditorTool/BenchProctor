// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ReconcileReceipt {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ReconcileReceipt")
    public void reconcileReceipt(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = java.util.Optional.ofNullable(System.getenv("INVENTORY_INPUT_0012")).orElse("");
        String backorder = normalize(phrase);
        Files.delete(Paths.get("/var/app/data/" + backorder));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
