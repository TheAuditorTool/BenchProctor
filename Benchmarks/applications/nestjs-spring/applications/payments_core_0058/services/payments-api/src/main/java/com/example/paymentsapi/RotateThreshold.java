// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.multipart.MultipartFile;

@RestController
class RotateThreshold {


    @PostMapping(path="/RotateThreshold", consumes="multipart/form-data")
    public void rotateThreshold(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = file != null ? file.getOriginalFilename() : "";
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", caption);
        String ledger = box.getProperty("value", "");
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(ledger);
        response.getWriter().print(node.path("name").asText());
    }
}
