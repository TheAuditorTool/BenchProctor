// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest63167 {

    @GET
    @Path("/BenchmarkTest63167")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest63167(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        if (!refererValue.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        Object evaluated = new jakarta.el.ELProcessor().eval(refererValue);
        return Response.ok("<div>" + evaluated + "</div>", MediaType.TEXT_HTML).build();
    }
}
