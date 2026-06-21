// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.xpath.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest61598 {

    private enum AllowedValue { ADMIN, OPERATOR, VIEWER, AUDITOR }

    @PostMapping(path="/BenchmarkTest61598", consumes="application/xml")
    public void BenchmarkTest61598(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        try { AllowedValue.valueOf(xmlValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { xmlValue = AllowedValue.values()[0].name().toLowerCase(); }
        XPathFactory xpf = XPathFactory.newInstance();
        XPath xpath = xpf.newXPath();
        xpath.evaluate("/users/user[@name='" + xmlValue + "']", new org.xml.sax.InputSource(new java.io.StringReader("<users/>")));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
