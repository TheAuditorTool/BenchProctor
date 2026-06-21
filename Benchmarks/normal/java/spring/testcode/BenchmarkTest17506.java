// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17506 {

    @PostMapping(path="/BenchmarkTest17506", consumes="application/xml")
    public void BenchmarkTest17506(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = xmlValue.replace("\u0000", "");
        if ("admin".equals(data) || "ROLE_ADMIN".equals(data)) {
            response.getWriter().print("{\"status\":\"ok\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
