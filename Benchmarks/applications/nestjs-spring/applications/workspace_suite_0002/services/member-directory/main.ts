import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { InviteMember } from "./member_invite";
import { ResolveThreshold } from "./resolve_threshold";
import { AuditIndex } from "./audit_index";
import { AuditRoster } from "./audit_roster";
import { ExportConfig } from "./export_config";
import { RenderSummary } from "./render_summary";
import { NormalizeSnapshot } from "./normalize_snapshot";
import { AuditCheckpoint } from "./audit_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, InviteMember, ResolveThreshold, AuditIndex, AuditRoster, ExportConfig, RenderSummary, NormalizeSnapshot, AuditCheckpoint],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
