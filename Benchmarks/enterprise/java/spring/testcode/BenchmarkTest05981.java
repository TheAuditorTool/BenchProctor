// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.xpath.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05981 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest05981")
    public void BenchmarkTest05981(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        holder.set(headerValue);
        String data = holder.get();
        if (!data.matches("^[\\w\\s./\\[\\]'\\\"=_-]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        XPathFactory xpf = XPathFactory.newInstance();
        XPath xpath = xpf.newXPath();
        xpath.evaluate("/users/user[@name='" + data + "']", new org.xml.sax.InputSource(new java.io.StringReader("<users/>")));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
