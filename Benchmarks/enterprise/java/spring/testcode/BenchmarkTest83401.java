// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest83401 {

    @GetMapping("/BenchmarkTest83401")
    public void BenchmarkTest83401(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        StringBuilder payload = new StringBuilder();
        payload.append(forwardedIp);
        String data = payload.toString();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
