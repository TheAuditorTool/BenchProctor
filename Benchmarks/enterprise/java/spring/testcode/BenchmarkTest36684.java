// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.xpath.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36684 {

    @GetMapping("/BenchmarkTest36684")
    public void BenchmarkTest36684(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data;
        if (authHeader.length() > 256) { data = authHeader.substring(0, 256); }
        else { data = authHeader; }
        XPathFactory xpf = XPathFactory.newInstance();
        XPath xpath = xpf.newXPath();
        xpath.evaluate("/users/user[@name='" + data + "']", new org.xml.sax.InputSource(new java.io.StringReader("<users/>")));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
