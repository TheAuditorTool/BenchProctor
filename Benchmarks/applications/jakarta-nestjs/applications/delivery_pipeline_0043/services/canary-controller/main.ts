import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { PromoteCanary } from "./canary_promote";
import { CollectThreshold } from "./collect_threshold";
import { PruneWindow } from "./prune_window";
import { VerifyReport } from "./verify_report";
import { PublishRecord } from "./publish_record";
import { BuildReceipt } from "./build_receipt";
import { RotatePolicy } from "./rotate_policy";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PromoteCanary, CollectThreshold, PruneWindow, VerifyReport, PublishRecord, BuildReceipt, RotatePolicy],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
