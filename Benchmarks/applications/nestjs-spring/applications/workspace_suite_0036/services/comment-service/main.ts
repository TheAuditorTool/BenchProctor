import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PostComment } from "./comment_post";
import { RotateSchedule } from "./rotate_schedule";
import { BuildPolicy } from "./build_policy";
import { NormalizeDocument } from "./normalize_document";
import { ValidateBundle } from "./validate_bundle";
import { SummarizeRecord } from "./summarize_record";
import { ValidateWorkspace } from "./validate_workspace";
import { PruneBatch } from "./prune_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PostComment, RotateSchedule, BuildPolicy, NormalizeDocument, ValidateBundle, SummarizeRecord, ValidateWorkspace, PruneBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
