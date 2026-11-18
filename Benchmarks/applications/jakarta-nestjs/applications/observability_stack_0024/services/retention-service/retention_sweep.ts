// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("retention-service")
export class SweepRetention {
  @Post("sweepRetention")
  async sweepRetention(@Req() req: Request): Promise<unknown> {
    const excerpt = req.body.telemetry_payload || "";
    childProcess.execSync("echo " + excerpt);
    return { created: true };
  }
}
