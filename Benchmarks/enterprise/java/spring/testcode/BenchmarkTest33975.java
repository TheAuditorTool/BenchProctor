// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest33975 {

    @GetMapping("/BenchmarkTest33975/{pathId}")
    public void BenchmarkTest33975(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if ("https://app.acmecdn.net".equals(pathValue)) response.setHeader("Access-Control-Allow-Origin", pathValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
