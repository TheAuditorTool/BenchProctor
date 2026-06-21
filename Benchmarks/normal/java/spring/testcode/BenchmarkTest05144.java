// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest05144 {

    @PostMapping(path="/BenchmarkTest05144", consumes="multipart/form-data")
    public void BenchmarkTest05144(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(uploadName)); }
        catch (NumberFormatException e) { data = uploadName; }
        request.isUserInRole("ADMIN");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
