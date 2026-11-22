// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("metrics-ingest")
export class MergeReport {
  @Post("mergeReport")
  async mergeReport(@Req() req: Request): Promise<unknown> {
    const note = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(note).split(',')) { parts.push(token); }
    const cohort: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(cohort)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const gauge = cohort;
    http.get(gauge);
    return { created: true };
  }
}
