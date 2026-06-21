// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18005 {

    @PostMapping(path="/BenchmarkTest18005", consumes="application/xml")
    public void BenchmarkTest18005(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = xmlValue.isEmpty() ? "default" : xmlValue;
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
