// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("knowledge-index")
export class ReconcileLedger {
  @Post("reconcileLedger")
  async reconcileLedger(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.host as string) || "";
    const grievance = `${citation}`;
    let _host = "";
    try { _host = new URL(String(grievance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const inquiry = grievance;
    http.get(inquiry);
    return { created: true };
  }
}
