import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { RegisterPartner } from "./partner_register";
import { EnrichConfig } from "./enrich_config";
import { PublishRoster } from "./publish_roster";
import { VerifyConnector } from "./verify_connector";
import { ArchiveHeader } from "./archive_header";
import { AuditWindow } from "./audit_window";
import { NormalizeIndex } from "./normalize_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RegisterPartner, EnrichConfig, PublishRoster, VerifyConnector, ArchiveHeader, AuditWindow, NormalizeIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
