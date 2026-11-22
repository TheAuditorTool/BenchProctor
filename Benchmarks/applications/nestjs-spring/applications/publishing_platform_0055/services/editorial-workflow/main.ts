import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { ReviewEditorial } from "./editorial_review";
import { ReconcileProfile } from "./reconcile_profile";
import { AuditLedger } from "./audit_ledger";
import { BuildSnapshot } from "./build_snapshot";
import { ExportRoster } from "./export_roster";
import { EnrichReport } from "./enrich_report";
import { SummarizeSummary } from "./summarize_summary";
import { AnnotateThreshold } from "./annotate_threshold";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ReviewEditorial, ReconcileProfile, AuditLedger, BuildSnapshot, ExportRoster, EnrichReport, SummarizeSummary, AnnotateThreshold],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
