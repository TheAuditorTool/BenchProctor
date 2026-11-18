// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("dashboard-api")
export class FormatDigest {
  @Post("formatDigest")
  async formatDigest(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const cohort: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(cohort)) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    return "<div>" + gauge + "</div>";
  }
}
