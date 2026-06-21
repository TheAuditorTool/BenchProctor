// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest43503 {

    @GET
    @Path("/BenchmarkTest43503")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest43503(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        if (!("true".equals(headerValue) || "false".equals(headerValue))) { return Response.status(400).build(); }
        request.getSession().setAttribute("data", String.valueOf(headerValue));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
