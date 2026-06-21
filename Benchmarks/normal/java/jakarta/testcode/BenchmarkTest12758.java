// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest12758 {

    @POST
    @Path("/BenchmarkTest12758")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12758(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.List<String> tokens = java.util.Arrays.asList(fieldValue.split(","));
        String data = String.join(",", tokens);
        byte[] buf = new byte[Integer.parseInt(data)];
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
