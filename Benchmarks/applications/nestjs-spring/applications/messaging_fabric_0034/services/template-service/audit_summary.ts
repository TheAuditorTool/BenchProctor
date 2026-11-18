// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("template-service")
export class AuditSummary {
  @Post("auditSummary")
  async auditSummary(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(footnote).split(',')) { parts.push(token); }
    const bulletin: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(bulletin)) { throw new BadRequestException({error:"invalid"}); }
    const heading = bulletin;
    return "<div>" + heading + "</div>";
  }
}
