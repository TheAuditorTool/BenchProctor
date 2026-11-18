import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RenderThumbnail } from "./thumbnail_render";
import { FetchLedger } from "./fetch_ledger";
import { BuildRoster } from "./build_roster";
import { RenderSchedule } from "./render_schedule";
import { AnnotateCaption } from "./annotate_caption";
import { LoadThreshold } from "./load_threshold";
import { RotateIndex } from "./rotate_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RenderThumbnail, FetchLedger, BuildRoster, RenderSchedule, AnnotateCaption, LoadThreshold, RotateIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
