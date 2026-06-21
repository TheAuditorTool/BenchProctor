// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80736 {

    @PostMapping(path="/BenchmarkTest80736", consumes="application/xml")
    public void BenchmarkTest80736(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = String.format("%s", xmlValue);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
