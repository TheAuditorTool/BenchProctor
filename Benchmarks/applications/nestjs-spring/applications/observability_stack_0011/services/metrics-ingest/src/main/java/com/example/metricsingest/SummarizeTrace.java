// SPDX-License-Identifier: Apache-2.0
package com.example.metricsingest;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class SummarizeTrace {


    @GetMapping("/SummarizeTrace")
    public void summarizeTrace(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = id != null ? id : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(caption, "query");
        String gauge = tuple.getKey();
        response.getWriter().print("<div>" + gauge + "</div>");
    }
}
