import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RegisterPartner } from "./partner_register";
import { CompactConfig } from "./compact_config";
import { LoadWindow } from "./load_window";
import { FormatPartner } from "./format_partner";
import { AuditReport } from "./audit_report";
import { EnrichSnapshot } from "./enrich_snapshot";
import { ExportSnapshot } from "./export_snapshot";
import { RotateDigest } from "./rotate_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RegisterPartner, CompactConfig, LoadWindow, FormatPartner, AuditReport, EnrichSnapshot, ExportSnapshot, RotateDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
