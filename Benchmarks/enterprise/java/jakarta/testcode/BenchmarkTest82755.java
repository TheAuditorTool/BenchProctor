// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest82755 {

    @GET
    @Path("/BenchmarkTest82755")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest82755(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        request.getSession().setAttribute("data", String.valueOf(forwardedIp));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
