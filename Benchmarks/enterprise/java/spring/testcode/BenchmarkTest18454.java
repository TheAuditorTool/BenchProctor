// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18454 {

    @GetMapping("/BenchmarkTest18454/{pathId}")
    public void BenchmarkTest18454(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        request.setAttribute("hidden_form_field", pathValue);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
