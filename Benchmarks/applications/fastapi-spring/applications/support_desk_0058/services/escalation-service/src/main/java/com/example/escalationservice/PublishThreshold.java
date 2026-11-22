// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class PublishThreshold {


    @PostMapping(path="/PublishThreshold", consumes="multipart/form-data")
    public void publishThreshold(@javax.validation.constraints.Size(max = 4096) @RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = multipartField != null ? multipartField : "";
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", snippet);
        String inquiry = box.getProperty("value", "");
        byte[] serBytes = java.util.Base64.getDecoder().decode(inquiry);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
