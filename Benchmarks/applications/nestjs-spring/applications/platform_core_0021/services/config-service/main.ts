import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RolloutConfig } from "./config_rollout";
import { ArchiveRoster } from "./archive_roster";
import { RenderQuota } from "./render_quota";
import { MergePolicy } from "./merge_policy";
import { ArchiveConfig } from "./archive_config";
import { RotateBundle } from "./rotate_bundle";
import { AuditHeader } from "./audit_header";
import { VerifyReceipt } from "./verify_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RolloutConfig, ArchiveRoster, RenderQuota, MergePolicy, ArchiveConfig, RotateBundle, AuditHeader, VerifyReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
