// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("recovery-service")
export class PublishConfig {
  @Post("publishConfig")
  async publishConfig(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(paragraph);
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const synopsis = persona;
    fs.unlinkSync("/var/app/data/" + synopsis);
    return { created: true };
  }
}
