// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("dashboard-api")
export class CollectReport {
  @Post("collectReport")
  async collectReport(@Req() req: Request): Promise<unknown> {
    const summary = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const cohort: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(cohort)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const gauge = cohort;
    http.get(gauge);
    return { created: true };
  }
}
