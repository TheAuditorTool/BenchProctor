// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest12636 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @POST
    @Path("/BenchmarkTest12636/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12636(@FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = toLowerCase(commentValue);
        if (System.currentTimeMillis() > 1000000000000L) {
            jakarta.el.ELProcessor elp = new jakarta.el.ELProcessor();
            Object rendered = elp.eval(data);
            return Response.ok("<div>" + rendered + "</div>", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
