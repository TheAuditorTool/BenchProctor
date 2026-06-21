// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52336 {

    private static String trimEnds(String v) { return v.trim(); }

    @PostMapping(path="/BenchmarkTest52336", consumes="application/xml")
    public void BenchmarkTest52336(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = trimEnds(xmlValue);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            System.loadLibrary(data);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
