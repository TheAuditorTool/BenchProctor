import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { DispatchCarrier } from "./carrier_dispatch";
import { RenderRoster } from "./render_roster";
import { FormatReceipt } from "./format_receipt";
import { RotateWaybill } from "./rotate_waybill";
import { PruneSummary } from "./prune_summary";
import { PublishPolicy } from "./publish_policy";
import { VerifyBundle } from "./verify_bundle";
import { ValidateSummary } from "./validate_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, DispatchCarrier, RenderRoster, FormatReceipt, RotateWaybill, PruneSummary, PublishPolicy, VerifyBundle, ValidateSummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
