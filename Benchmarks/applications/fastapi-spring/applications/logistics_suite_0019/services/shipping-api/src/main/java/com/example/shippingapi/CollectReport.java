// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class CollectReport {


    @GetMapping("/CollectReport/{pathId}")
    public void collectReport(@javax.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = pathId;
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(citation, "query");
        String parcel = edge.getKey();
        new ProcessBuilder("echo", parcel).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
