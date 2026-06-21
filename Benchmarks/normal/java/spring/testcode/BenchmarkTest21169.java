// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest21169 {

    @PostMapping(path="/BenchmarkTest21169", consumes="application/xml")
    public void BenchmarkTest21169(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = String.format("payload=%s", xmlValue);
        response.setHeader("Refresh", "0; url=" + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
