// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
public class BenchmarkTest02991 {

    @POST
    @Path("/BenchmarkTest02991")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02991(@FormDataParam("multipart_field") String multipartField, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = String.format("payload=%s", multipartValue);
        java.nio.file.Path resolvedBase = java.nio.file.Paths.get("/var/app/data").toAbsolutePath();
        java.nio.file.Path requested = resolvedBase.resolve(data).normalize();
        if (!requested.startsWith(resolvedBase)) { return Response.status(403).entity("outside safe scope").build(); }
        Runtime.getRuntime().exec(new String[]{"chown", "appuser:appgroup", requested.toString()}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok().build();
    }
}
