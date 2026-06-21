// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14577 {

    @PostMapping(path="/BenchmarkTest14577", consumes="application/xml")
    public void BenchmarkTest14577(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        request.getSession().setAttribute("data", String.valueOf(xmlValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
