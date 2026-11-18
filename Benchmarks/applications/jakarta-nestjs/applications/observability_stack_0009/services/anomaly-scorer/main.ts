import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ScoreAnomaly } from "./anomaly_score";
import { BuildPolicy } from "./build_policy";
import { ReconcileRoster } from "./reconcile_roster";
import { CompactDigest } from "./compact_digest";
import { FetchTrace } from "./fetch_trace";
import { ReconcileBundle } from "./reconcile_bundle";
import { FormatDigest } from "./format_digest";
import { AuditConfig } from "./audit_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ScoreAnomaly, BuildPolicy, ReconcileRoster, CompactDigest, FetchTrace, ReconcileBundle, FormatDigest, AuditConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
