// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04223 {

    @GetMapping("/BenchmarkTest04223")
    public void BenchmarkTest04223(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(headerValue);
        String processed = org.owasp.encoder.Encode.forHtml(data);
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + processed + "\">");
    }
}
