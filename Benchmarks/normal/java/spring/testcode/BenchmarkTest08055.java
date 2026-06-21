// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08055 {

    @PostMapping(path="/BenchmarkTest08055", consumes="application/xml")
    public void BenchmarkTest08055(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = String.format("%s", xmlValue);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
