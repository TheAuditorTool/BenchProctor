// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18796 {

    @GetMapping("/BenchmarkTest18796/{pathId}")
    public void BenchmarkTest18796(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data;
        try { data = String.valueOf(Integer.parseInt(pathValue)); }
        catch (NumberFormatException e) { data = pathValue; }
        request.setAttribute("hidden_form_field", data);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
