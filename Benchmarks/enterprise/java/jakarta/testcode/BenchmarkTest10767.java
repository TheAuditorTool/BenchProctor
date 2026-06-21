// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10767 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @POST
    @Path("/BenchmarkTest10767")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10767(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = collapseWhitespace(fieldValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        return Response.ok("{\"resource\":\"" + processed + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
