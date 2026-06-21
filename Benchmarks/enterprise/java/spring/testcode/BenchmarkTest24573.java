// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest24573 {

    @PostMapping(path="/BenchmarkTest24573", consumes="multipart/form-data")
    public void BenchmarkTest24573(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        response.addCookie(new Cookie("session", uploadName));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
