// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest83148 {

    @PostMapping(path="/BenchmarkTest83148", consumes="application/xml")
    public void BenchmarkTest83148(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = "" + xmlValue;
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + data}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
