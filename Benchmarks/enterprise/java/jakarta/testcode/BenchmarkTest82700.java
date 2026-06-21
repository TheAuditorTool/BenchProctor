// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest82700 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @POST
    @Path("/BenchmarkTest82700/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest82700(@FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        try { AllowedValue.valueOf(commentValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { commentValue = AllowedValue.values()[0].name().toLowerCase(); }
        new ProcessBuilder("python3", "-c", commentValue).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
