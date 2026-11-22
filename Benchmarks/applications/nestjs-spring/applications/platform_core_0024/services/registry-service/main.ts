import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { RegisterService } from "./service_register";
import { PublishSnapshot } from "./publish_snapshot";
import { LoadRecord } from "./load_record";
import { ResolveBundle } from "./resolve_bundle";
import { RotateRecord } from "./rotate_record";
import { PublishCheckpoint } from "./publish_checkpoint";
import { CollectReport } from "./collect_report";
import { LoadReceipt } from "./load_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RegisterService, PublishSnapshot, LoadRecord, ResolveBundle, RotateRecord, PublishCheckpoint, CollectReport, LoadReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
