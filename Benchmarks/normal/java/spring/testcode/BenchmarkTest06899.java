// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06899 {

    @GetMapping("/BenchmarkTest06899")
    public void BenchmarkTest06899(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(headerValue);
        String data = wrapper.toString();
        if (!data.matches("^[\\w\\s.\\-:/=\\r\\n]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        response.setHeader("Access-Control-Allow-Origin", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
