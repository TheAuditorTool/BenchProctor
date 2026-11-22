// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("knowledge-index")
export class EnrichThreshold {
  @Post("enrichThreshold")
  async enrichThreshold(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["user-agent"] as string) || "";
    let _host = "";
    try { _host = new URL(String(remark)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const grievance = remark;
    http.get(grievance);
    return { created: true };
  }
}
