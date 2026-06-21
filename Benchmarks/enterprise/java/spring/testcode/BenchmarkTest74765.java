// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest74765 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping(path="/BenchmarkTest74765", consumes="application/xml")
    public void BenchmarkTest74765(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        holder.set(xmlValue);
        String data = holder.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.getWriter().print("{\"resource\":\"" + processed + "\"}");
    }
}
