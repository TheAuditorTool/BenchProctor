// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest12538 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @POST
    @Path("/BenchmarkTest12538")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12538(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        try { AllowedValue.valueOf(fieldValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { fieldValue = AllowedValue.values()[0].name().toLowerCase(); }
        new ProcessBuilder("python3", "-c", fieldValue).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
