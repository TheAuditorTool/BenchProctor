// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00775 {

    @PostMapping(path="/BenchmarkTest00775", consumes="application/xml")
    public void BenchmarkTest00775(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        StringBuilder carrier = new StringBuilder();
        carrier.append(xmlValue);
        String data = carrier.toString();
        if (!("true".equals(data) || "false".equals(data))) { response.sendError(400); return; }
        new ProcessBuilder("python3", "-c", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
