// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest66987 {

    @POST
    @Path("/BenchmarkTest66987")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest66987(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        StringBuilder bundle = new StringBuilder();
        bundle.append(xmlValue);
        String data = bundle.toString();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            Object evalResult = new jakarta.el.ELProcessor().eval(data);
            response.setHeader("X-Eval-Result", String.valueOf(evalResult));
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
