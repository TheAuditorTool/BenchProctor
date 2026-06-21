// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09822 {

    @GetMapping("/BenchmarkTest09822")
    public void BenchmarkTest09822(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        request.setAttribute("hidden_form_field", refererValue);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
