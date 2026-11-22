import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ValidateAddress } from "./address_validate";
import { NormalizeIndex } from "./normalize_index";
import { ResolveRoster } from "./resolve_roster";
import { RotateHeader } from "./rotate_header";
import { NormalizeWindow } from "./normalize_window";
import { RotateSnapshot } from "./rotate_snapshot";
import { CollectManifest } from "./collect_manifest";
import { PruneProfile } from "./prune_profile";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ValidateAddress, NormalizeIndex, ResolveRoster, RotateHeader, NormalizeWindow, RotateSnapshot, CollectManifest, PruneProfile],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
