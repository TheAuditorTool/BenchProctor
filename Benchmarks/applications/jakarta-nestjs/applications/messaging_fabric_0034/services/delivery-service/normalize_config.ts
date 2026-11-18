// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("delivery-service")
export class NormalizeConfig {
  @Post("normalizeConfig")
  async normalizeConfig(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return footnote; } };
    const bulletin = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const heading = bulletin;
    const fileContent = fs.readFileSync("/var/app/data/" + heading, "utf8");
    return fileContent;
  }
}
