// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest44865 {

    @PostMapping(path="/BenchmarkTest44865", consumes="text/plain")
    public void BenchmarkTest44865(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(rawData);
        String data = normalizer.apply(rawData);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(processed)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
