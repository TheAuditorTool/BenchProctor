import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ShipLog } from "./log_ship";
import { ResolveLedger } from "./resolve_ledger";
import { MergeReport } from "./merge_report";
import { ReconcileSchedule } from "./reconcile_schedule";
import { ResolveWindow } from "./resolve_window";
import { RotateDigest } from "./rotate_digest";
import { MergeReceipt } from "./merge_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ShipLog, ResolveLedger, MergeReport, ReconcileSchedule, ResolveWindow, RotateDigest, MergeReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
