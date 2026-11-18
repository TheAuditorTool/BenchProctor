// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileThreshold {


    @GetMapping("/ReconcileThreshold/{pathId}")
    public void reconcileThreshold(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = pathId;
        String parcel = java.net.URLDecoder.decode(citation, java.nio.charset.StandardCharsets.UTF_8);
        String consignment = parcel.matches("^(plain|markdown|html|text)$") ? parcel : "plain";
        response.getWriter().print("<div>" + consignment + "</div>");
    }
}
