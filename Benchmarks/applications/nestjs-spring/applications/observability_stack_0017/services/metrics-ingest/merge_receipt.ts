// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("metrics-ingest")
export class MergeReceipt {
  @Post("mergeReceipt")
  async mergeReceipt(@Req() req: Request): Promise<unknown> {
    const note = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(note).split(',').filter((t) => t.length > 0);
    const cohort = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(cohort)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const gauge = cohort;
    http.get(gauge);
    return { created: true };
  }
}
