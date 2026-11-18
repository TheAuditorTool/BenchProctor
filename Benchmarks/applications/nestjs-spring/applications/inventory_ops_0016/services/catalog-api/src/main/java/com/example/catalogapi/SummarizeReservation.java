// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.multipart.MultipartFile;

@RestController
class SummarizeReservation {


    @PostMapping(path="/SummarizeReservation", consumes="multipart/form-data")
    public void summarizeReservation(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = file != null ? file.getOriginalFilename() : "";
        java.util.Properties container = new java.util.Properties();
        container.setProperty("value", citation);
        String backorder = container.getProperty("value", "");
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(backorder);
        response.getWriter().print(node.path("name").asText());
    }
}
