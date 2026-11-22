import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { ApplyRedaction } from "./redaction_apply";
import { RotateBundle } from "./rotate_bundle";
import { PublishThreshold } from "./publish_threshold";
import { NormalizeReport } from "./normalize_report";
import { VerifySnapshot } from "./verify_snapshot";
import { ValidateIndex } from "./validate_index";
import { ReconcileThreshold } from "./reconcile_threshold";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ApplyRedaction, RotateBundle, PublishThreshold, NormalizeReport, VerifySnapshot, ValidateIndex, ReconcileThreshold],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
