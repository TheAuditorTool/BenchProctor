// SPDX-License-Identifier: Apache-2.0
package com.example.addressvalidator;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class SummarizeLabel {


    @GetMapping("/SummarizeLabel")
    public void summarizeLabel(@javax.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = id != null ? id : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : summary.split(",")) { tokens.add(token.trim()); }
        String consignment = String.join(",", tokens);
        response.getWriter().print("<div>" + consignment + "</div>");
    }
}
