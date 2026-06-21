// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52699 {

    @PostMapping(path="/BenchmarkTest52699", consumes="application/xml")
    public void BenchmarkTest52699(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = String.format("payload=%s", xmlValue);
        try {
            Integer.parseInt(data);
        } catch (Exception e) { }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
