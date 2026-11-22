import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { EnforceQuota } from "./quota_enforce";
import { BuildPolicy } from "./build_policy";
import { ReconcilePolicy } from "./reconcile_policy";
import { CollectThreshold } from "./collect_threshold";
import { FormatSchedule } from "./format_schedule";
import { LoadPolicy } from "./load_policy";
import { ValidateQuota } from "./validate_quota";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, EnforceQuota, BuildPolicy, ReconcilePolicy, CollectThreshold, FormatSchedule, LoadPolicy, ValidateQuota],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
