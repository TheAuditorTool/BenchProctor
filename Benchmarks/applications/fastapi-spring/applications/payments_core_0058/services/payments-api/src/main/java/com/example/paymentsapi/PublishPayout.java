// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PublishPayout {


    @GetMapping("/PublishPayout/{pathId}")
    public void publishPayout(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = pathId;
        String ledger;
        if (caption.length() > 256) { ledger = caption.substring(0, 256); }
        else { ledger = caption; }
        response.getWriter().print("<div>" + ledger + "</div>");
    }
}
