// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("template-service")
export class ValidateMessage {
  @Post("validateMessage")
  async validateMessage(@Req() req: Request): Promise<unknown> {
    const subject = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const bulletin: string = normalize(subject);
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const passage = bulletin;
    fs.unlinkSync("/var/app/data/" + passage);
    return { created: true };
  }
}
