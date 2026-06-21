// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12634 {

    @GetMapping("/BenchmarkTest12634")
    public void BenchmarkTest12634(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = "[%s]".formatted(hostValue);
        String processed = org.owasp.encoder.Encode.forHtml(data);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
