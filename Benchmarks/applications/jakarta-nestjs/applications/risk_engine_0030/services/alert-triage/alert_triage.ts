// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("alert-triage")
export class TriageAlert {
  @Post("triageAlert")
  async triageAlert(@Req() req: Request): Promise<unknown> {
    const headline = req.body.risk_payload || "";
    fs.writeFileSync("/var/uploads/" + headline, "data");
    return { created: true };
  }
}
