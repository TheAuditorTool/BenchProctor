// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest55038 {

    private static final java.util.concurrent.atomic.AtomicReference<String> ref = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping(path="/BenchmarkTest55038", consumes="application/xml")
    public void BenchmarkTest55038(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        ref.set(xmlValue);
        String data = ref.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        request.setAttribute("hidden_form_field", processed);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
