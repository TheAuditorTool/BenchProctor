// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("capture-service")
export class SummarizeProfile {
  @Post("summarizeProfile")
  async summarizeProfile(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(caption).split(',')) { parts.push(token); }
    const ledger: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(ledger)) { throw new BadRequestException({error:"invalid"}); }
    const remittance = ledger;
    return "<div>" + remittance + "</div>";
  }
}
