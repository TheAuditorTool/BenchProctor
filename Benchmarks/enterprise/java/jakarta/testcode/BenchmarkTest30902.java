// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.security.*;

@Path("/")
public class BenchmarkTest30902 {

    @GET
    @Path("/BenchmarkTest30902")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest30902(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : refererValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        byte[] staticSalt = "bench_static_1234".getBytes();
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(staticSalt);
        byte[] digest = md.digest(data.getBytes());
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
