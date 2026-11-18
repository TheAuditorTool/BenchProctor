import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SolveAllocation } from "./allocation_solve";
import { AuditSupplier } from "./audit_supplier";
import { SummarizeAllocation } from "./summarize_allocation";
import { ValidateSchedule } from "./validate_schedule";
import { ReconcileConfig } from "./reconcile_config";
import { ReconcileDigest } from "./reconcile_digest";
import { MergeThreshold } from "./merge_threshold";
import { PruneAllocation } from "./prune_allocation";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SolveAllocation, AuditSupplier, SummarizeAllocation, ValidateSchedule, ReconcileConfig, ReconcileDigest, MergeThreshold, PruneAllocation],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
