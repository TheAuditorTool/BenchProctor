import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RouteTicket } from "./ticket_route";
import { EnrichMacro } from "./enrich_macro";
import { AnnotateLedger } from "./annotate_ledger";
import { ResolveRoster } from "./resolve_roster";
import { AuditSummary } from "./audit_summary";
import { ReconcileProfile } from "./reconcile_profile";
import { ArchiveThreshold } from "./archive_threshold";
import { BuildLedger } from "./build_ledger";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RouteTicket, EnrichMacro, AnnotateLedger, ResolveRoster, AuditSummary, ReconcileProfile, ArchiveThreshold, BuildLedger],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
