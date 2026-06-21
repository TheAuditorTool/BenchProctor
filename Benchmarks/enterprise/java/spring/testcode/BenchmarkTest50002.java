// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50002 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest50002")
    public void BenchmarkTest50002(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = trimEnds(userId);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
