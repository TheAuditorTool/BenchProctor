// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("attachment-store")
export class SummarizeBundle {
  @Post("summarizeBundle")
  async summarizeBundle(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const inquiry: string = transform(snippet);
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(inquiry)) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    fs.writeFileSync("/var/uploads/" + grievance, "data");
    return { created: true };
  }
}
