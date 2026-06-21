// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18132 {

    @GET
    @Path("/BenchmarkTest18132")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18132(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(refererValue);
        String data = bundle.toString();
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
