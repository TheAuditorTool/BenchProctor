// SPDX-License-Identifier: Apache-2.0
package com.example.documentapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class LoadReceipt {


    @PostMapping("/LoadReceipt")
    public void loadReceipt(@javax.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = field != null ? field : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(wording, "form");
        String addendum = entry.getKey();
        String dossier = addendum.matches("^(status|info|list|show)$") ? addendum : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + dossier});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
