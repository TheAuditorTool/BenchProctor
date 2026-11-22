// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("device-trust")
export class ReconcileSummary {
  @Post("reconcileSummary")
  async reconcileSummary(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body?.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(paragraph).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const blurb = persona;
    fs.unlinkSync("/var/app/data/" + blurb);
    return { created: true };
  }
}
