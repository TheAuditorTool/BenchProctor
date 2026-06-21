// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14545 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GetMapping("/BenchmarkTest14545")
    public void BenchmarkTest14545(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        FormData payload = new FormData(headerValue);
        String data = payload.payload;
        if (!data.isEmpty()) throw new Exception("processing error: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
