// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("dashboard-api")
export class QueryDashboard {
  @Post("queryDashboard")
  async queryDashboard(@Req() req: Request): Promise<unknown> {
    const quotation = req.body.telemetry_payload || "";
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(quotation));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const gauge = _parsed.data;
    childProcess.execSync("echo " + gauge);
    return { created: true };
  }
}
