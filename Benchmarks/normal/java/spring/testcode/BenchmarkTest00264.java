// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00264 {

    @GetMapping("/BenchmarkTest00264")
    public void BenchmarkTest00264(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = "" + userId;
        response.getWriter().print(String.valueOf(data));
    }
}
