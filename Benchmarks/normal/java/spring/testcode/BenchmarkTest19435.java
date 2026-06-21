// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest19435 {

    @PostMapping(path="/BenchmarkTest19435", consumes="application/xml")
    public void BenchmarkTest19435(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = "[%s]".formatted(xmlValue);
        String processed = org.owasp.encoder.Encode.forHtml(data);
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + processed + "\">");
    }
}
