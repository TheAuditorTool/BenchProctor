// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12633 {

    @GetMapping("/BenchmarkTest12633")
    public void BenchmarkTest12633(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = String.join(" ", userId.split("\\s+"));
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
