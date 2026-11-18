import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { OpenDispute } from "./dispute_open";
import { RotateMandate } from "./rotate_mandate";
import { ResolveIndex } from "./resolve_index";
import { EnrichWallet } from "./enrich_wallet";
import { AuditReport } from "./audit_report";
import { MergeIndex } from "./merge_index";
import { CompactCheckpoint } from "./compact_checkpoint";
import { ArchiveProfile } from "./archive_profile";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, OpenDispute, RotateMandate, ResolveIndex, EnrichWallet, AuditReport, MergeIndex, CompactCheckpoint, ArchiveProfile],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
