// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest46657 {

    @POST
    @Path("/BenchmarkTest46657/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest46657(@FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String prefix = commentValue.length() > 0 ? commentValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = commentValue.toLowerCase(); break;
            case "f": data = commentValue.toUpperCase(); break;
            default: data = commentValue.strip(); break;
        }
        if (!("true".equals(data) || "false".equals(data))) { return Response.status(400).build(); }
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
