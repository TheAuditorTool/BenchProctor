import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RunSettlement } from "./settlement_batch";
import { ResolveSnapshot } from "./resolve_snapshot";
import { CompactReceipt } from "./compact_receipt";
import { RotateReport } from "./rotate_report";
import { PruneReport } from "./prune_report";
import { ValidateSchedule } from "./validate_schedule";
import { FetchSchedule } from "./fetch_schedule";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunSettlement, ResolveSnapshot, CompactReceipt, RotateReport, PruneReport, ValidateSchedule, FetchSchedule],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
