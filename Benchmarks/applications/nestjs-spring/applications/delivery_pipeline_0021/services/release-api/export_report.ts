// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("release-api")
export class ExportReport {
  @Post("exportReport")
  async exportReport(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.host as string) || "";
    const phrase = summary != null ? summary : '';
    if (!/^(asc|desc|name|created)$/.test(String(phrase))) { throw new BadRequestException({error:"invalid"}); }
    const subtitle = phrase;
    fs.writeFileSync("/var/uploads/" + subtitle, "data");
    return { created: true };
  }
}
