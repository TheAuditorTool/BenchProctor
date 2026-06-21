// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest55064 {

    @GetMapping("/BenchmarkTest55064")
    public void BenchmarkTest55064(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String processed = org.owasp.encoder.Encode.forHtml(hostValue);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
