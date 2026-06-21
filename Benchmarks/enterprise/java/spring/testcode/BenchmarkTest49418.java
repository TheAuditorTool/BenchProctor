// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49418 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping(path="/BenchmarkTest49418", consumes="application/xml")
    public void BenchmarkTest49418(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        stateBox.set(xmlValue);
        String data = stateBox.get();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            new Socket(data, 80).close();
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
