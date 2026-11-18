// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("upload-gateway")
export class EnrichReport {
  @Post("enrichReport")
  async enrichReport(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return transcript; } };
    const rendition = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(rendition))) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    const fileContent = fs.readFileSync("/var/app/data/" + montage, "utf8");
    return fileContent;
  }
}
