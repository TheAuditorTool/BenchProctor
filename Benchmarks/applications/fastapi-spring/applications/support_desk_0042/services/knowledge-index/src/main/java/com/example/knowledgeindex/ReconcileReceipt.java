// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileReceipt {


    @PostMapping("/ReconcileReceipt")
    public void reconcileReceipt(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String blurb = field != null ? field : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(blurb, "form");
        String inquiry = entry.getKey();
        String grievance = inquiry.matches("^(status|info|list|show)$") ? inquiry : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + grievance});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
