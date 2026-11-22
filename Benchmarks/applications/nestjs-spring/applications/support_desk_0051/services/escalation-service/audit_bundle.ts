// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("escalation-service")
export class AuditBundle {
  @Post("auditBundle")
  async auditBundle(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["x-forwarded-for"] as string) || "";
    const grievance = preface != null ? preface : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(grievance)) { throw new BadRequestException({error:"invalid"}); }
    const inquiry = grievance;
    return "<div>" + inquiry + "</div>";
  }
}
