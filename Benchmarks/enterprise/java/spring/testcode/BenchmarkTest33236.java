// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest33236 {

    @PostMapping(path="/BenchmarkTest33236", consumes="multipart/form-data")
    public void BenchmarkTest33236(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        StringBuilder payload = new StringBuilder();
        payload.append(multipartValue);
        String data = payload.toString();
        jakarta.servlet.http.HttpSession existingSession = request.getSession(false);
        if (existingSession == null || existingSession.getAttribute("user") == null) {
            response.sendError(401, "no session"); return;
        }
        request.getSession().setAttribute("data", String.valueOf(data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
