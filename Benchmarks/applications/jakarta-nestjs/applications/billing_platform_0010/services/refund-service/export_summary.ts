// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("refund-service")
export class ExportSummary {
  @Post("exportSummary")
  async exportSummary(@Req() req: Request): Promise<unknown> {
    const headline = (req.cookies?.session_token as string) || "";
    const remittance = headline != null ? headline : '';
    let _host = "";
    try { _host = new URL(String(remittance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dunning = remittance;
    http.get(dunning);
    return { created: true };
  }
}
