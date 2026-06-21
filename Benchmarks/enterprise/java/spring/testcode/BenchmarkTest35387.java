// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35387 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest35387")
    public void BenchmarkTest35387(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = stripCRLF(originValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(processed)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
