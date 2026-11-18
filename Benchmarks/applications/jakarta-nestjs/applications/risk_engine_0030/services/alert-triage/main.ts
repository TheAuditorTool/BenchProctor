import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { TriageAlert } from "./alert_triage";
import { EnrichSchedule } from "./enrich_schedule";
import { CompactRoster } from "./compact_roster";
import { BuildDecision } from "./build_decision";
import { ReconcileBatch } from "./reconcile_batch";
import { ArchiveSchedule } from "./archive_schedule";
import { ArchiveRule } from "./archive_rule";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, TriageAlert, EnrichSchedule, CompactRoster, BuildDecision, ReconcileBatch, ArchiveSchedule, ArchiveRule],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
