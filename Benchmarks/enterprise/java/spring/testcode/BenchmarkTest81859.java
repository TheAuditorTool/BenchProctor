// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81859 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest81859", consumes="application/xml")
    public void BenchmarkTest81859(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = stripWhitespace(xmlValue);
        int divisor = Integer.parseInt(data);
        if (divisor == 0) { response.sendError(400); return; }
        int result = 100 / divisor;
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
