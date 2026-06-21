// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18529 {

    @GET
    @Path("/BenchmarkTest18529")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18529(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.Properties property = new java.util.Properties();
        property.load(new java.io.StringReader("rawValue=" + authHeader.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", property.getProperty("format", "plain"));
        String data = property.getProperty("rawValue", "");
        response.setHeader("X-Frame-Options", "DENY");
        response.setHeader("Content-Security-Policy", "frame-ancestors 'none'");
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
