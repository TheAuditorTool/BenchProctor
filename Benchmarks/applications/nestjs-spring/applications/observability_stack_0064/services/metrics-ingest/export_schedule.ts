// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("metrics-ingest")
export class ExportSchedule {
  @Post("exportSchedule")
  async exportSchedule(@Req() req: Request): Promise<unknown> {
    const tagline = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(tagline).split(',').filter((t) => t.length > 0);
    const gauge = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(gauge)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const cohort = gauge;
    http.get(cohort);
    return { created: true };
  }
}
