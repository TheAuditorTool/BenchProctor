// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest19735 {

    @GetMapping("/BenchmarkTest19735/{pathId}")
    public void BenchmarkTest19735(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        request.getSession().setAttribute("data", String.valueOf(pathValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
