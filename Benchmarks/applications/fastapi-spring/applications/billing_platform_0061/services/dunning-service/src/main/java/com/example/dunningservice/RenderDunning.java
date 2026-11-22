// SPDX-License-Identifier: Apache-2.0
package com.example.dunningservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class RenderDunning {


    @PostMapping("/RenderDunning")
    public void renderDunning(@javax.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = field != null ? field : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(footnote, "cookie");
        String remittance = tuple.getKey();
        String arrears = remittance.matches("^(status|info|list|show)$") ? remittance : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + arrears});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
