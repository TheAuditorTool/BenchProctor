// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("attachment-store")
export class ExportPolicy {
  @Post("exportPolicy")
  async exportPolicy(@Req() req: Request): Promise<unknown> {
    const blurb = (req.headers["x-forwarded-for"] as string) || "";
    const inquiry = blurb != null ? blurb : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(inquiry)) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    return "<div>" + grievance + "</div>";
  }
}
