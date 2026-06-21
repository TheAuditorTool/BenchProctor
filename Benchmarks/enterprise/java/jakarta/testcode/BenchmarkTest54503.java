// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest54503 {

    @GET
    @Path("/BenchmarkTest54503")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest54503(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        return Response.ok("<div>" + forwardedIp + "</div>", MediaType.TEXT_HTML).build();
    }
}
