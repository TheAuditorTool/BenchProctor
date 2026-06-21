// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest19797 {

    @GetMapping("/BenchmarkTest19797")
    public void BenchmarkTest19797(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(originValue)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
