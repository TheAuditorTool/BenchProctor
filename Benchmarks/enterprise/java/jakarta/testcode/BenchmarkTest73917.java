// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest73917 {

    @POST
    @Path("/BenchmarkTest73917")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest73917(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.function.Function<String, String> firstStage = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::trim);
        String data = composed.apply(rawData);
        String processed = data.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
        return Response.ok(processed + ",data\n", "text/csv").build();
    }
}
