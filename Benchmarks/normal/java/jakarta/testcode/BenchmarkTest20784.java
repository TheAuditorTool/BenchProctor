// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest20784 {

    @POST
    @Path("/BenchmarkTest20784")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest20784(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(fieldValue);
        String data = wrapper.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + processed + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
