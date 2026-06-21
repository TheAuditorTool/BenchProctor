// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest19467 {

    @GetMapping("/BenchmarkTest19467")
    public void BenchmarkTest19467(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        StringBuilder bundle = new StringBuilder();
        bundle.append(envValue);
        String data = bundle.toString();
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
