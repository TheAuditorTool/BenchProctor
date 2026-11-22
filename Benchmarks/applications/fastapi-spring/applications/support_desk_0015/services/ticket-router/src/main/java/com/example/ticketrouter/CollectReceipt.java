// SPDX-License-Identifier: Apache-2.0
package com.example.ticketrouter;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
class CollectReceipt {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/CollectReceipt", consumes="multipart/form-data")
    public void collectReceipt(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = file != null ? file.getOriginalFilename() : "";
        String grievance = normalize(phrase);
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(grievance)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
