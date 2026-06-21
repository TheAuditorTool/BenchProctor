// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12094 {

    @PostMapping(path="/BenchmarkTest12094", consumes="application/xml")
    public void BenchmarkTest12094(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = xmlValue.isEmpty() ? "default" : xmlValue;
        try {
            Integer.parseInt(data);
        } catch (Exception ignored) {
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
