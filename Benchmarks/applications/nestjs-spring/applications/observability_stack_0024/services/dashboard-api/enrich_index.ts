// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("dashboard-api")
export class EnrichIndex {
  @Post("enrichIndex")
  async enrichIndex(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const cohort: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(cohort)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const gauge = cohort;
    net.connect(80, new URL(String(gauge)).hostname);
    return { created: true };
  }
}
