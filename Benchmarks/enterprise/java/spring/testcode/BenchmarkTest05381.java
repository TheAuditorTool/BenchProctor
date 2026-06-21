// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05381 {

    @PostMapping(path="/BenchmarkTest05381", consumes="application/xml")
    public void BenchmarkTest05381(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = xmlValue.replace("\u0000", "");
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) { response.sendError(400); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
