// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest72318 {

    @PostMapping(path="/BenchmarkTest72318", consumes="multipart/form-data")
    public void BenchmarkTest72318(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        try {
            Integer.parseInt(uploadName);
        } catch (NumberFormatException e) { response.sendError(400); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
