// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16205 {

    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @POST
    @Path("/BenchmarkTest16205")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16205(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        try { AllowedValue.valueOf(fieldValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { fieldValue = AllowedValue.values()[0].name().toLowerCase(); }
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + fieldValue + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
