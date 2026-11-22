import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { RunCycleCount } from "./cycle_count";
import { SummarizeHeader } from "./summarize_header";
import { AuditStock } from "./audit_stock";
import { AnnotateSnapshot } from "./annotate_snapshot";
import { AnnotateSchedule } from "./annotate_schedule";
import { BuildSnapshot } from "./build_snapshot";
import { EnrichLedger } from "./enrich_ledger";
import { ArchiveLedger } from "./archive_ledger";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunCycleCount, SummarizeHeader, AuditStock, AnnotateSnapshot, AnnotateSchedule, BuildSnapshot, EnrichLedger, ArchiveLedger],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
