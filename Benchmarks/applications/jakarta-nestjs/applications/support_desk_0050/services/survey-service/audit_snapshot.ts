// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("survey-service")
export class AuditSnapshot {
  @Post("auditSnapshot")
  async auditSnapshot(@Req() req: Request): Promise<unknown> {
    const remark = (req.body as string) || "";
    const inquiry = Buffer.from(remark, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(inquiry)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const grievance = inquiry;
    http.get(grievance);
    return { created: true };
  }
}
