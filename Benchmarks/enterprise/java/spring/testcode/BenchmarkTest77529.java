// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest77529 {

    @GetMapping("/BenchmarkTest77529")
    public void BenchmarkTest77529(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
        dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
        dbf.setFeature(javax.xml.XMLConstants.FEATURE_SECURE_PROCESSING, true);
        dbf.setExpandEntityReferences(false);
        dbf.newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(headerValue)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
