// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest68301 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @POST
    @Path("/BenchmarkTest68301/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest68301(@FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = collapseWhitespace(commentValue);
        String processed = data.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
        return Response.ok(processed + ",data\n", "text/csv").build();
    }
}
