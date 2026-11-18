// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("case-service")
export class ArchiveLedger {
  @Post("archiveLedger")
  async archiveLedger(@Req() req: Request): Promise<unknown> {
    const subject = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(subject).split(',')) { parts.push(token); }
    const grievance: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(grievance)) { throw new BadRequestException({error:"invalid"}); }
    const verdict = grievance;
    return "<div>" + verdict + "</div>";
  }
}
