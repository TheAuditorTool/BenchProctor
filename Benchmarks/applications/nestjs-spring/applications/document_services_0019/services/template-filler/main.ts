import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { FillTemplate } from "./template_fill";
import { VerifyRoster } from "./verify_roster";
import { AuditRecord } from "./audit_record";
import { CompactLedger } from "./compact_ledger";
import { VerifyBundle } from "./verify_bundle";
import { ResolveProfile } from "./resolve_profile";
import { ArchiveBatch } from "./archive_batch";
import { AnnotateConfig } from "./annotate_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, FillTemplate, VerifyRoster, AuditRecord, CompactLedger, VerifyBundle, ResolveProfile, ArchiveBatch, AnnotateConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
