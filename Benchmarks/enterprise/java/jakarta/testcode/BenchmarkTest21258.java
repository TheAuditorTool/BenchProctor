// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
public class BenchmarkTest21258 {

    @POST
    @Path("/BenchmarkTest21258")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21258(@FormDataParam("multipart_field") String multipartField, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(multipartValue);
        String data = envelope.toString();
        if (!data.matches("^[\\w\\s<>\\\"'/().;=]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
