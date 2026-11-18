// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("attachment-store")
export class AuditSurvey {
  @Post("auditSurvey")
  async auditSurvey(@Req() req: Request): Promise<unknown> {
    const remark = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(remark);
    const inquiry: string = readInput();
    let _host = "";
    try { _host = new URL(String(inquiry)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const grievance = inquiry;
    http.get(grievance);
    return { created: true };
  }
}
