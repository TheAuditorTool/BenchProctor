// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08118 {

    @PostMapping(path="/BenchmarkTest08118", consumes="application/xml")
    public void BenchmarkTest08118(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = "" + xmlValue;
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) {
            response.sendError(400, e.getMessage()); return;
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
