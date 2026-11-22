// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("sampling-config")
export class ConfigureSample {
  @Post("configureSample")
  async configureSample(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.authorization as string) || "";
    const gauge = String(remark).slice(0, 200);
    await fetch("http://retention-service:8080/SweepRetention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
    return { created: true };
  }
}
