// SPDX-License-Identifier: Apache-2.0
package com.example.anomalyscorer;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class BuildPolicy {


    @GetMapping("/BuildPolicy")
    public void buildPolicy(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = id != null ? id : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(summary, "json");
        String gauge = edge.getKey();
        response.getWriter().print("<div>" + gauge + "</div>");
    }
}
