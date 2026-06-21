// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16574 {

    @GET
    @Path("/BenchmarkTest16574")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16574(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(forwardedIp)); }
        catch (NumberFormatException e) { data = forwardedIp; }
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
