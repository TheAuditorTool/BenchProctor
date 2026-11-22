// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class FormatWindow {


    @PostMapping("/FormatWindow")
    public void formatWindow(@javax.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = field != null ? field : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String disbursement = transform.apply(headline);
        String remittance = disbursement.matches("^(status|info|list|show)$") ? disbursement : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + remittance});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
