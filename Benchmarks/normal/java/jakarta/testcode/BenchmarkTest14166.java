// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest14166 {

    @GET
    @Path("/BenchmarkTest14166")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest14166(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        response.setHeader("Access-Control-Allow-Origin", forwardedIp);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
