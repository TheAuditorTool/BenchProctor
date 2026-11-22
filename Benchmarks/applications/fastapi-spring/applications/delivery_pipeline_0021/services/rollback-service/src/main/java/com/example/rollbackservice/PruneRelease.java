// SPDX-License-Identifier: Apache-2.0
package com.example.rollbackservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class PruneRelease {


    @PostMapping(path="/PruneRelease", consumes="multipart/form-data")
    public void pruneRelease(@javax.validation.constraints.Size(max = 4096) @RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = multipartField != null ? multipartField : "";
        java.util.Properties container = new java.util.Properties();
        container.setProperty("value", summary);
        String phrase = container.getProperty("value", "");
        byte[] serBytes = java.util.Base64.getDecoder().decode(phrase);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
