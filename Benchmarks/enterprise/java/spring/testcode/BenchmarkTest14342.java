// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14342 {

    @PostMapping(path="/BenchmarkTest14342", consumes="application/xml")
    public void BenchmarkTest14342(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(xmlValue, "body");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        int divisor = Integer.parseInt(data);
        if (divisor == 0) { response.sendError(400); return; }
        int result = 100 / divisor;
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
