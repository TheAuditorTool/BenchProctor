// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("presence-service")
export class NormalizeRecord {
  @Post("normalizeRecord")
  async normalizeRecord(@Req() req: Request): Promise<unknown> {
    const subject = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return subject; } };
    const bulletin = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const passage = bulletin;
    const fileContent = fs.readFileSync("/var/app/data/" + passage, "utf8");
    return fileContent;
  }
}
