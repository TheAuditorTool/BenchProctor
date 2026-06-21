// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04709 {

    @PostMapping(path="/BenchmarkTest04709", consumes="application/xml")
    public void BenchmarkTest04709(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String processed = org.owasp.encoder.Encode.forHtml(xmlValue);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
