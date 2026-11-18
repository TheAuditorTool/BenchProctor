// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("session-store")
export class FormatCheckpoint {
  @Post("formatCheckpoint")
  async formatCheckpoint(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return paragraph; } };
    const persona = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const synopsis = persona;
    const fileContent = fs.readFileSync("/var/app/data/" + synopsis, "utf8");
    return fileContent;
  }
}
