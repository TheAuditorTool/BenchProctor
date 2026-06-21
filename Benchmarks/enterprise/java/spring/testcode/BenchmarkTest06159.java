// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06159 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @PostMapping(path="/BenchmarkTest06159", consumes="application/xml")
    public void BenchmarkTest06159(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = collapseWhitespace(xmlValue);
        try {
            Integer.parseInt(data);
        } catch (Exception ignored) {
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
