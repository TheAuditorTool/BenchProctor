// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("registry-service")
export class SummarizeDigest {
  @Post("summarizeDigest")
  async summarizeDigest(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(subtitle).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    fs.unlinkSync("/var/app/data/" + handshake);
    return { created: true };
  }
}
