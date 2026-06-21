// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest44494 {

    @GET
    @Path("/BenchmarkTest44494")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest44494(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(forwardedIp);
        String data = wrapper.toString();
        return Response.status(500).entity(data).build();
    }
}
