import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RaiseEscalation } from "./escalation_raise";
import { LoadBundle } from "./load_bundle";
import { AuditManifest } from "./audit_manifest";
import { AnnotateSummary } from "./annotate_summary";
import { PruneSummary } from "./prune_summary";
import { EnrichTicket } from "./enrich_ticket";
import { ResolveTicket } from "./resolve_ticket";
import { ReconcileTicket } from "./reconcile_ticket";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RaiseEscalation, LoadBundle, AuditManifest, AnnotateSummary, PruneSummary, EnrichTicket, ResolveTicket, ReconcileTicket],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
