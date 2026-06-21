// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest77484 {

    @PostMapping(path="/BenchmarkTest77484", consumes="application/xml")
    public void BenchmarkTest77484(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = String.format("payload=%s", xmlValue);
        request.getSession().setAttribute("data", String.valueOf(data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
