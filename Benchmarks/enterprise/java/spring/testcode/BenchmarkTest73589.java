// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73589 {

    @PostMapping(path="/BenchmarkTest73589", consumes="application/xml")
    public void BenchmarkTest73589(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = xmlValue.replace("\u0000", "");
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
