// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76286 {

    @GetMapping("/BenchmarkTest76286")
    public void BenchmarkTest76286(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = "" + forwardedIp;
        String processed = org.owasp.encoder.Encode.forHtml(data);
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + processed + "\">");
    }
}
