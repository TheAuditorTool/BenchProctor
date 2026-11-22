package com.example.statementexport;

public class JakartaBootstrap {

    @jakarta.ws.rs.Path("/health")
    public static class HealthResource {
        @jakarta.ws.rs.GET
        public jakarta.ws.rs.core.Response health() {
            return jakarta.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.statementexport.JakartaBootstrap$HealthResource,com.example.statementexport.BuildStatement,com.example.statementexport.MergeSummary,com.example.statementexport.ReconcileWindow,com.example.statementexport.ResolveHeader,com.example.statementexport.SummarizeSummary,com.example.statementexport.ValidateCheckpoint,com.example.statementexport.ValidateSchedule,com.example.statementexport.ValidateWindow");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
