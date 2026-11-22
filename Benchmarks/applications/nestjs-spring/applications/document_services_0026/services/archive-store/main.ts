import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { StoreArchive } from "./archive_store";
import { AuditIndex } from "./audit_index";
import { ArchiveDigest } from "./archive_digest";
import { PublishManifest } from "./publish_manifest";
import { BuildProfile } from "./build_profile";
import { ValidateCheckpoint } from "./validate_checkpoint";
import { ReconcileCheckpoint } from "./reconcile_checkpoint";
import { ResolveRoster } from "./resolve_roster";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, StoreArchive, AuditIndex, ArchiveDigest, PublishManifest, BuildProfile, ValidateCheckpoint, ReconcileCheckpoint, ResolveRoster],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
