// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09678 {

    @POST
    @Path("/BenchmarkTest09678")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09678(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String prefix = fieldValue.length() > 0 ? fieldValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = fieldValue.toLowerCase(); break;
            case "f": data = fieldValue.toUpperCase(); break;
            default: data = fieldValue.strip(); break;
        }
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
