// SPDX-License-Identifier: Apache-2.0
package com.example.paymentgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.multipart.MultipartFile;

@RestController
class BuildSummary {


    @PostMapping(path="/BuildSummary", consumes="multipart/form-data")
    public void buildSummary(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = file != null ? file.getOriginalFilename() : "";
        java.util.Properties store = new java.util.Properties();
        store.setProperty("value", remark);
        String remittance = store.getProperty("value", "");
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(remittance);
        response.getWriter().print(node.path("name").asText());
    }
}
