// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("sampling-config")
export class ConfigureSample {
  @Post("configureSample/:id")
  async configureSample(@Req() req: Request): Promise<unknown> {
    const preface = (req.params.id as string) || "";
    const cohort = preface != null ? preface : '';
    await fetch("http://retention-service:8080/SweepRetention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
    return { created: true };
  }
}
