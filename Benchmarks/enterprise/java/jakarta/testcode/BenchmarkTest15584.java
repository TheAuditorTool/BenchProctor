// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest15584 {

    @POST
    @Path("/BenchmarkTest15584")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest15584(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data;
        if (fieldValue.length() > 256) { data = fieldValue.substring(0, 256); }
        else { data = fieldValue; }
        return Response.ok("{\"resource\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
