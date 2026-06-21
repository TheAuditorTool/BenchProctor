// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest30009 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest30009")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest30009(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = normalize(forwardedIp);
        new java.io.File("/tmp/" + data).createNewFile();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
