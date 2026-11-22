import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { CheckSla } from "./sla_check";
import { PruneReceipt } from "./prune_receipt";
import { ResolveSnapshot } from "./resolve_snapshot";
import { RotateCheckpoint } from "./rotate_checkpoint";
import { VerifyRoster } from "./verify_roster";
import { RenderCheckpoint } from "./render_checkpoint";
import { PrunePolicy } from "./prune_policy";
import { FetchManifest } from "./fetch_manifest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CheckSla, PruneReceipt, ResolveSnapshot, RotateCheckpoint, VerifyRoster, RenderCheckpoint, PrunePolicy, FetchManifest],
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
