// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("settlement-service")
export class EnrichRecord {
  @Post("enrichRecord")
  async enrichRecord(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(footnote).split(',')) { parts.push(token); }
    const remittance: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(remittance))) { throw new BadRequestException({error:"invalid"}); }
    const arrears = remittance;
    fs.unlinkSync("/var/app/data/" + arrears);
    return { created: true };
  }
}
