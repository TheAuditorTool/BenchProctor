// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09941 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @POST
    @Path("/BenchmarkTest09941/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09941(@FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = stripCRLF(commentValue);
        if (!data.matches("^[\\w\\s.,;:_/\\-=]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        return Response.ok("{\"resource\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
