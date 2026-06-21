// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest12431 {

    @POST
    @Path("/BenchmarkTest12431")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12431(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(xmlValue, "request");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        Object evalResult = new jakarta.el.ELProcessor().eval(data);
        response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
