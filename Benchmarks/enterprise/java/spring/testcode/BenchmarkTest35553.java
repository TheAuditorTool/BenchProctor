// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35553 {

    @GetMapping("/BenchmarkTest35553/{pathId}")
    public void BenchmarkTest35553(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + pathValue + "\">");
    }
}
