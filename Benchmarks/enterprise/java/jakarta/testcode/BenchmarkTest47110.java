// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest47110 {

    @GET
    @Path("/BenchmarkTest47110")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest47110(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = String.format("payload=%s", uaValue);
        java.security.MessageDigest md = java.security.MessageDigest.getInstance("SHA-256");
        byte[] hashed = md.digest(data.getBytes());
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(java.util.Base64.getEncoder().encodeToString(hashed));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
