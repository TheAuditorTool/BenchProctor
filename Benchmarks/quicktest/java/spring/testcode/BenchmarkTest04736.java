// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04736 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest04736", consumes="application/xml")
    public void BenchmarkTest04736(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = normalize(xmlValue);
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(data)) { response.sendError(403); return; }
        String allowedBin = data;
        System.loadLibrary(allowedBin);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
