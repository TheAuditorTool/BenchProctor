// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("sampling-config")
export class LoadMetric {
  @Post("loadMetric")
  async loadMetric(@Req() req: Request): Promise<unknown> {
    const paragraph = ((req as any).files?.[0]?.originalname as string) || "";
    const parts: string[] = [];
    for (const token of String(paragraph).split(',')) { parts.push(token); }
    const gauge: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(gauge)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const cohort = gauge;
    const outbound = { method: "get", url: String(cohort), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
