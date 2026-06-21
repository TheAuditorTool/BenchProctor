// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16988 {

    @PostMapping(path="/BenchmarkTest16988", consumes="application/xml")
    public void BenchmarkTest16988(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data;
        if (xmlValue.length() > 256) { data = xmlValue.substring(0, 256); }
        else { data = xmlValue; }
        if ("admin".equals(data) || "ROLE_ADMIN".equals(data)) {
            response.getWriter().print("{\"status\":\"ok\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
