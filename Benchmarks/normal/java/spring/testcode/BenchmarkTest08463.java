// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08463 {

    @GetMapping("/BenchmarkTest08463")
    public void BenchmarkTest08463(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        if (!cookieValue.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        int[] arr = new int[]{10, 20, 30, 40, 50};
        int idx = Integer.parseInt(cookieValue);
        response.setHeader("X-Lookup", String.valueOf(arr[idx]));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
