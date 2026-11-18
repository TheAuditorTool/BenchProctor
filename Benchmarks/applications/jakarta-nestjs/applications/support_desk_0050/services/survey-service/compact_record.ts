// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("survey-service")
export class CompactRecord {
  @Post("compactRecord")
  async compactRecord(@Req() req: Request): Promise<unknown> {
    const remark = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return remark; } };
    const inquiry = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(inquiry))) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    const fileContent = fs.readFileSync("/var/app/data/" + grievance, "utf8");
    return fileContent;
  }
}
