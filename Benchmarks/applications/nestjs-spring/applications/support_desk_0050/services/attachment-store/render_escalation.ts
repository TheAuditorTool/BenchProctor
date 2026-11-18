// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("attachment-store")
export class RenderEscalation {
  @Post("renderEscalation")
  async renderEscalation(@Req() req: Request): Promise<unknown> {
    const remark = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const inquiry: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(inquiry)) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    return "<div>" + grievance + "</div>";
  }
}
