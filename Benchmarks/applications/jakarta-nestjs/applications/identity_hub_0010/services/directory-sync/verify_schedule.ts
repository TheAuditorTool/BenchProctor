// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("directory-sync")
export class VerifySchedule {
  @Post("verifySchedule")
  async verifySchedule(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return phrase; } };
    const persona = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const transcript = persona;
    const fileContent = fs.readFileSync("/var/app/data/" + transcript, "utf8");
    return fileContent;
  }
}
