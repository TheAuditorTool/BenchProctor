// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71214 {

    @PostMapping(path="/BenchmarkTest71214", consumes="multipart/form-data")
    public void BenchmarkTest71214(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(multipartValue);
        String data = wrapper.toString();
        if (data.length() > 2048) { response.sendError(400, "schema invalid"); return; }
        response.addCookie(new Cookie("session", data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
