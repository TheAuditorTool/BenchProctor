// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest74874 {

    @PostMapping(path="/BenchmarkTest74874", consumes="application/xml")
    public void BenchmarkTest74874(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(xmlValue);
        request.setAttribute("hidden_form_field", data);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
