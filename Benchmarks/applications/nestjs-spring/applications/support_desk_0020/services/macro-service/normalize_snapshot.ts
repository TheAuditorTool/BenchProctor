// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("macro-service")
export class NormalizeSnapshot {
  @Post("normalizeSnapshot")
  async normalizeSnapshot(@Req() req: Request): Promise<unknown> {
    const phrase = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const inquiry: string = normalize(phrase);
    if (!/^(asc|desc|name|created)$/.test(String(inquiry))) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    fs.unlinkSync("/var/app/data/" + grievance);
    return { created: true };
  }
}
