// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("dashboard-api")
export class BuildThreshold {
  @Post("buildThreshold")
  async buildThreshold(@Req() req: Request): Promise<unknown> {
    const headline = ((req as any).file?.originalname as string) || "";
    let cohort;
    try { cohort = JSON.parse(headline).value || headline; }
    catch (e) { cohort = headline; }
    nodeSerialize.unserialize(cohort);
    return { created: true };
  }
}
