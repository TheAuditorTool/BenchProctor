// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest33601 {

    @GET
    @Path("/BenchmarkTest33601/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest33601(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.nio.file.Files.write(java.nio.file.Paths.get("plugins/generated.js"), ("var setting = '" + pathValue + "';").getBytes());
        javax.script.ScriptEngine engine = new javax.script.ScriptEngineManager().getEngineByName("nashorn");
        engine.eval(new java.io.FileReader("plugins/generated.js"));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
