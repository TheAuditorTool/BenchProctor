// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18242 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GET
    @Path("/BenchmarkTest18242")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18242(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = expandTabs(headerValue);
        if (!data.matches("^[\\w\\s.,;:_/\\-=]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
