// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest45108 {

    @PostMapping(path="/BenchmarkTest45108", consumes="application/xml")
    public void BenchmarkTest45108(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = String.format("payload=%s", xmlValue);
        if (!data.isEmpty()) throw new Exception("processing error: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
