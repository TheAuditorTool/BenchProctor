// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest48696 {

    @PostMapping(path="/BenchmarkTest48696", consumes="text/plain")
    public void BenchmarkTest48696(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String processed = org.owasp.encoder.Encode.forHtml(rawData);
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + processed + "\">");
    }
}
