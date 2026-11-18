import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ShipLog } from "./log_ship";
import { LoadSchedule } from "./load_schedule";
import { ResolveWindow } from "./resolve_window";
import { VerifyIndex } from "./verify_index";
import { NormalizeAlert } from "./normalize_alert";
import { LoadThreshold } from "./load_threshold";
import { RotatePolicy } from "./rotate_policy";
import { MergeSummary } from "./merge_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ShipLog, LoadSchedule, ResolveWindow, VerifyIndex, NormalizeAlert, LoadThreshold, RotatePolicy, MergeSummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
