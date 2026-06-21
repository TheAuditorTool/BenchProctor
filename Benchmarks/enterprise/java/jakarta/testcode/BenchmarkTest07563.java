// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest07563 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GET
    @Path("/BenchmarkTest07563")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest07563(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = collapseWhitespace(refererValue);
        if (!data.matches("^[\\w\\s.,;:_/\\-=]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
