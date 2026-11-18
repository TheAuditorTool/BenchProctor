// SPDX-License-Identifier: Apache-2.0
package com.example.settlementservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.multipart.MultipartFile;

@RestController
class ValidateSchedule {


    @PostMapping(path="/ValidateSchedule", consumes="multipart/form-data")
    public void validateSchedule(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = file != null ? file.getOriginalFilename() : "";
        java.util.Properties container = new java.util.Properties();
        container.setProperty("value", remark);
        String remittance = container.getProperty("value", "");
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(remittance);
        response.getWriter().print(node.path("name").asText());
    }
}
