// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.xpath.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest31467 {

    @PostMapping(path="/BenchmarkTest31467", consumes="text/plain")
    public void BenchmarkTest31467(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(rawData);
        String data = bundle.toString();
        if (System.currentTimeMillis() > 1000000000000L) {
            XPathFactory xpf = XPathFactory.newInstance();
            XPath xpath = xpf.newXPath();
            xpath.evaluate("/users/user[@name='" + data + "']", new org.xml.sax.InputSource(new java.io.StringReader("<users/>")));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
