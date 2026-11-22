package com.example.editorialworkflow;

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
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.editorialworkflow.JakartaBootstrap$HealthResource,com.example.editorialworkflow.AuditLedger,com.example.editorialworkflow.BuildBundle,com.example.editorialworkflow.FormatBundle,com.example.editorialworkflow.ReconcileProfile,com.example.editorialworkflow.RenderThreshold,com.example.editorialworkflow.ReviewEditorial,com.example.editorialworkflow.SummarizeConfig,com.example.editorialworkflow.ValidatePolicy");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
