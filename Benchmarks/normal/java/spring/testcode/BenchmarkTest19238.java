// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest19238 {

    @PostMapping("/BenchmarkTest19238")
    public void BenchmarkTest19238(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(fieldValue);
        String data = envelope.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(processed);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
