// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest78121 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @POST
    @Path("/BenchmarkTest78121")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest78121(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = stripWhitespace(fieldValue);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            response.getWriter().print("<div>" + data + "</div>");
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok().build();
    }
}
