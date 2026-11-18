import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { OpenDispute } from "./dispute_open";
import { RotateRoster } from "./rotate_roster";
import { AnnotateReport } from "./annotate_report";
import { AuditLedger } from "./audit_ledger";
import { EnrichRoster } from "./enrich_roster";
import { FormatWindow } from "./format_window";
import { FetchPolicy } from "./fetch_policy";
import { FetchManifest } from "./fetch_manifest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, OpenDispute, RotateRoster, AnnotateReport, AuditLedger, EnrichRoster, FormatWindow, FetchPolicy, FetchManifest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
