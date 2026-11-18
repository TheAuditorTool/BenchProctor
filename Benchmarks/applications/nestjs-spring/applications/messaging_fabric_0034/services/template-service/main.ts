import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ComposeTemplate } from "./template_compose";
import { CompactSchedule } from "./compact_schedule";
import { SummarizeSnapshot } from "./summarize_snapshot";
import { ResolveManifest } from "./resolve_manifest";
import { ArchiveSummary } from "./archive_summary";
import { AuditSummary } from "./audit_summary";
import { VerifyBundle } from "./verify_bundle";
import { CompactIndex } from "./compact_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ComposeTemplate, CompactSchedule, SummarizeSnapshot, ResolveManifest, ArchiveSummary, AuditSummary, VerifyBundle, CompactIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
