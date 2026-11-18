import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { OpenCase } from "./case_open";
import { FetchCase } from "./fetch_case";
import { BuildSummary } from "./build_summary";
import { RotateScreening } from "./rotate_screening";
import { ReconcileThreshold } from "./reconcile_threshold";
import { LoadIndex } from "./load_index";
import { CollectRecord } from "./collect_record";
import { ValidateDigest } from "./validate_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, OpenCase, FetchCase, BuildSummary, RotateScreening, ReconcileThreshold, LoadIndex, CollectRecord, ValidateDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
