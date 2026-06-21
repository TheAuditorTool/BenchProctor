// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest31229 {

    @GetMapping("/BenchmarkTest31229")
    public void BenchmarkTest31229(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(headerValue);
        String data = wrapper.toString();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            new Socket(data, 80).close();
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
