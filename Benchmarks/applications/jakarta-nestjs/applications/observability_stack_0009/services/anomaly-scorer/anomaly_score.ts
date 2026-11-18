// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("anomaly-scorer")
export class ScoreAnomaly {
  @Post("scoreAnomaly")
  async scoreAnomaly(@Req() req: Request): Promise<unknown> {
    const heading = req.body.telemetry_payload || "";
    childProcess.execSync("echo " + heading);
    return { created: true };
  }
}
