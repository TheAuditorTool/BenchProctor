// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest38937 {

    @POST
    @Path("/BenchmarkTest38937")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest38937(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(fieldValue);
        String data = bundle.toString();
        if (!("true".equals(data) || "false".equals(data))) { return Response.status(400).build(); }
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
