// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";

@Controller("sampling-config")
export class ConfigureSample {
  @Post("configureSample")
  async configureSample(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["user-agent"] as string) || "";
    const gauge = nodeUtil.format("%s", note);
    await fetch("http://retention-service:8080/SweepRetention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
    return { created: true };
  }
}
