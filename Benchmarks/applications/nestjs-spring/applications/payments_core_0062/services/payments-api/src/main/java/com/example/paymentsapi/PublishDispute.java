// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PublishDispute {


    @GetMapping("/PublishDispute/{pathId}")
    public void publishDispute(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = pathId;
        String disbursement;
        if (headline.length() > 256) { disbursement = headline.substring(0, 256); }
        else { disbursement = headline; }
        response.setContentType("text/html;charset=UTF-8");
        response.getOutputStream().write(("<div class=\"comment\">" + disbursement + "</div>").getBytes(java.nio.charset.StandardCharsets.UTF_8));
    }
}
