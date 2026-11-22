// SPDX-License-Identifier: Apache-2.0
package com.example.ticketrouter;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class EnrichTicket {


    @PostMapping("/EnrichTicket")
    public void enrichTicket(@javax.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = field != null ? field : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(phrase, "request");
        String grievance = pair.getKey();
        String inquiry = grievance.matches("^(status|info|list|show)$") ? grievance : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + inquiry});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
