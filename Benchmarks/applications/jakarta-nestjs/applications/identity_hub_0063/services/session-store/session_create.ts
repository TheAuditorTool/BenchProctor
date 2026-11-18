// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("session-store")
export class CreateSession {
  @Post("createSession")
  async createSession(@Req() req: Request): Promise<unknown> {
    const transcript = req.body.identity_payload || "";
    if (!/^(asc|desc|name|created)$/.test(String(transcript))) { throw new BadRequestException({error:"invalid"}); }
    const synopsis = transcript;
    const fileContent = fs.readFileSync("/var/app/data/" + synopsis, "utf8");
    return fileContent;
  }
}
